#encoding: utf-8
import scrapy
import re
import urllib
from urllib import urlopen
from scrapy.selector import Selector
from IR_news_proj.items import *
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule

class chinanewsSpider(CrawlSpider):
    name = "chinanews"
    allowed_domains = ["www.chinanews.com"]
    start_urls = ['http://www.chinanews.com/sports.shtml']
    rules=(
        Rule(LinkExtractor(allow = r"/ty/\d+/\d{0,3}-\d{0,3}/\d+.*shtml"),
        callback="parse_news",follow=True),
    )

    '''def printcn(suni):
        for i in uni:
            print uni.encode('utf-8')
    '''
    def parse_news(self,response):
        item = IrNewsProjItem()
        item['news_thread'] = response.url.strip().split('/')[-1][:-6]

        self.get_title(response,item)
        self.get_source(response,item)
        self.get_url(response,item)
        self.get_news_from(response,item)
        self.get_text(response,item)
        self.get_hot(response,item)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!remenber to Retrun Item after parse
        return item

    def get_title(self,response,item):
        title = response.xpath('//*[@id="cont_1_1_2"]/h1/text()').extract()
        if title:
            #print 'title:' + title[0]
            item['news_title'] = title[0]

    def get_source(self,response,item):
        source=response.xpath('//*[@id="cont_1_1_2"]/div[4]/div[1]/text()').extract()
        if source:
            #print 'source' + source[0][0:19]
            item['news_time']=source[0][0:19]

    def get_news_from(self,response,item):
        news_from = response.xpath('//*[@id="cont_1_1_2"]/div[4]/div[1]/text()').extract()
        if news_from:
            #print 'from' + news_from[0][19:]
            item['news_from']=news_from[0][19:]

    ''' text Yeap!  '''

    def  get_text(self,response,item):
        news_body=response.xpath("//*[@class='left_zw']//p/text()").extract()
        if news_body:
            #for  entry in news_body:
                #print entry.encode('utf-8')
            item['news_body']=news_body

    ''' url Yeap!  '''

    def get_url(self,response,item):
        news_url=response.url
        if news_url:
            #print news_url
            item['news_url'] = news_url

    ''' hot Yeap!  '''

    def get_hot(self, response,item):
        item['news_hot'] = 0
        newsid = response.xpath('//*[@id="newsid"]/@value').extract()
        newsdate = response.xpath('//*[@id="newsdate"]/@value').extract()
        hoturl = 'http://mood.chinanews.com.cn/data/' + newsdate[0].replace(r'-', r'/') + '/' + newsid[0] + '.shtml'
        f = urlopen(hoturl)
        content = f.read()
        #print 'hoturl : ' + hoturl + '\n hoturl: ' + response.url + '\n hoturl: ' +content
        if content:
            pattern = re.compile(r'"total":.*,')
            match = pattern.search(content)
            if match:
                item['news_hot'] = match.group()
                item['news_hot'] = item['news_hot'][8:-1]
        print 'news_hot: ' + str(item['news_hot'])




