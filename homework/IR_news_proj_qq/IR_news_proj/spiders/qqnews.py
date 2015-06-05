#encoding: utf-8
import scrapy
import re
import urllib2
from urllib import urlopen
from scrapy.selector import Selector
from IR_news_proj.items import *
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
import random

class qqnewsSpider(CrawlSpider):
    name = "qqnews"
    allowed_domains = ["sports.qq.com"]
    start_urls = ['http://sports.qq.com/a/20051222/000402.htm']
    rules=(
        Rule(LinkExtractor(allow = r"/a/\d+/\d+.*htm"),
        callback="parse_news",follow=True),
    )

    '''def printcn(suni):
        for i in uni:
            print uni.encode('utf-8')
    '''
    def parse_news(self,response):
        item = IrNewsProjItem()
        item['news_thread'] = response.url.strip().split('/')[-1][:6]
        
        url = self.get_url(response,item)
        self.get_title(response,item)
        self.get_time(response,item)
        self.get_news_from(response,item)
        news_body = self.get_text(response,item)
        self.get_hot(response, item)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!remenber to Retrun Item after parse
        if urllib2.urlopen(url).geturl() == url or news_body != None:
            return item

    def get_title(self,response,item):
        title = response.xpath('//h1/text()|//*[@id="ArticleTit"]/text()|//*[@id="ArtTit"]/text()').extract()
        if title:
            print 'title:' + title[0]
            item['news_title'] = title[0]

    def get_time(self,response,item):
        hxs  = HtmlXPathSelector(response)
        time = hxs.re(r'(\d{4}).?.?(\d{2}).?.?(\d{2}).?.?.?.?(\d{2}):(\d{2})')
        time = str(time[0]) + '-' + str(time[1]) + '-' + str(time[2]) + ' ' + str(time[3]) + ':' + str(time[4]) + ':' + str('%02d'%(random.randint(0, 59)))
        item['news_time'] = time
        print 'time: ', time

    def get_news_from(self,response,item):
        news_from = response.xpath('//*[@id="C-Main-Article-QQ"]/div[1]/div[1]/div[1]/span[1]/a/text()|//*[@id="ArtFrom"]/a[2]/text()').extract()
        if news_from:
            print 'from' + news_from[0]
            item['news_from']=news_from[0]
        else:
            item['news_from']= '腾讯专稿'


    def  get_text(self,response,item):
        news_body=response.xpath('//*[@id="Cnt-Main-Article-QQ"]/p/text()|//*[@id="Cnt-Main-Article-QQ"]/p//a/text()|//*[@id="ArticleCnt"]/p/text()|//*[@id="ArtCnt"]/p/text()').extract()
        if news_body:
            #for  entry in news_body:
            #print entry.encode('utf-8')
            item['news_body']=news_body
        else:
            item['news_body'] = ['图表、视频或者表格']
        return news_body

    def get_url(self,response,item):
        news_url=response.url
        if news_url:
            print news_url
            item['news_url'] = news_url
            return news_url

    def get_hot(self, response, item):
        hxs  = HtmlXPathSelector(response)
        match = hxs.re(r'cmt_id = \d+;')
        cmt_id = ''
        hot = 0
        if match:
            aa = match[0]
            cmt_id = match[0][9:-1]
            print 'match: ' + cmt_id
            hoturl = 'http://coral.qq.com/article/' + cmt_id + '/commentnum?callback=_cbSum&source=1&t=123'
            f = urlopen(hoturl)
            content = f.read()
            #print 'match: ' + content
            pattern = re.compile(r'"commentnum":"\d+"')
            match = pattern.search(content)
            if match:
                hot = match.group()
                hot = hot[14:-1]
        #print 'match: ' + hot
        item['news_hot'] = hot
        #print 'item_match: ' , item['news_hot']

