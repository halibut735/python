# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import urllib2

class IrNewsProjPipeline(object):
    def __init__(self):
        #self.file = codecs.open('163.json', 'w', encoding='utf-8')
        self.count = 20000

    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line.decode('unicode_escape'))
        
        filename = 'hupu/' + str(self.count) + '.txt'
        self.count += 1
        file = codecs.open(filename, 'w', encoding='utf-8')

        redirectUrl = urllib2.urlopen(item['news_url']).geturl()
        if redirectUrl != item['news_url']:
            return item
        
        if item['news_url'] or True:
            url = 'URL=' + item['news_url'] + '\r\n'
            file.write(url)
        
        if item['news_time'] or True:
            time = 'Time=' + item['news_time'] + '\r\n'
            file.write(time)
        if item['news_hot'] or True:
            hot = 'Comment=' + str(item['news_hot'][:-16])
            file.write(hot)
            file.write('\r\n')
        if item['news_title'] or True:
            title = '标题=' + item['news_title'][:-8]
            file.write(title)
            file.write('\r\n')
        if item['news_body'] or True:
            body = '正文='
            file.write(body)
            body = item['news_body']
            for each in body:
                file.write(each)
            file.write('\r\n')
        return item
