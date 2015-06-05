#encoding: utf-8
import scrapy
import re
from scrapy.selector import Selector
from IR_news_proj.items import *
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
import urllib
import sys
import HTMLParser
import urlparse
import urllib
import urllib2


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class hupuNewsSpider(CrawlSpider):
    name = "hupunews"
    allowed_domains = ["voice.hupu.com"]
    start_urls = ['http://www.hupu.com/']
    rules=(
        Rule(LinkExtractor(allow = r"/.*/\d+.html.*"),
        callback="parse_news",follow=True),
    )


    def parse_news(self,response):
        item = IrNewsProjItem()
        item['news_thread'] = response.url.strip().split('/')[-1][:7]

        self.get_title(response,item)
        self.get_time(response,item)
        self.get_url(response,item)
        self.get_news_from(response,item)
        #self.get_summary(response, item)
        self.get_text(response,item)
        self.get_hot(response, item)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!remenber to Retrun Item after parse
        return item
    

    def get_title(self,response,item):
        title = response.xpath('//h1/text()').extract()
        if title:
            print 'title: ' + title[0][14:]
            item['news_title'] = title[0][14:]

    def get_time(self,response,item):
        
        hxs  = HtmlXPathSelector(response)
        time = hxs.re(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
        time = time[0]
        item['news_time'] = time
        print 'time: ' + time

    def get_news_from(self,response,item):
        news_from = response.xpath('//*[@id="source_baidu"]/a/text()').extract()
        if news_from:
            print 'from: ' + news_from[0]
            item['news_from'] = news_from[0]

    def get_summary(self, response, item):
        summary = response.xpath('//*[@id="epContentLeft"]/p/text()').extract()
        if summary:
            print 'summary: ' + summary[0]
            item['news_summary'] = summary[0]

    def  get_text(self,response,item):
        news_body=response.xpath('//*[@class="artical-main-content"]/p//text()').extract()
        
        if news_body:
            for  entry in news_body:
                print 'paragraph: ' + entry
        item['news_body'] = news_body
        '''if item['news_summary'] == None:
            item['news_summary'] = item['news_body'][:2]'''

    def get_url(self,response,item):
        news_url=response.url
        if news_url:
            print 'url: ' + news_url
            item['news_url'] = news_url

    def get_hot(self, response, item):
        
        hot = response.xpath('//*[@class="btn-viewComment"]/text()').extract()
        if hot:
            print 'news_hot: ' + hot[1][22:]
            item['news_hot'] = hot[1][22:]
        
        '''hxs  = HtmlXPathSelector(response)
        hot = hxs.re(r'totalCount = .*,')
        hot = hot[0]
        pattern = re.compile(r'=.*,')
        hot = pattern.search(hot).group()
        hot = hot[2:-1]
        news_hot = hot
        if news_hot:
            print 'hot or comments: ' + news_hot
            item['news_hot'] = news_hot'''
