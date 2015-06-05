# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
class IrNewsProjPipeline(object):
    def __init__(self):
        #self.file = codecs.open('163.json', 'w', encoding='utf-8')
        self.count = 0

    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line.decode('unicode_escape'))
        
        filename = str(self.count) + '.txt'
        self.count += 1
        file = codecs.open(filename, 'w', encoding='utf-8')
        if item['news_url']:
            url = 'URL=' + item['news_url'] + '\r\n'
            file.write(url)
        if item['news_time']:
            time = 'Time=' + item['news_time'] + '\r\n'
            file.write(time)
        if item['news_hot'] or item['news_hot'] == 0:
            hot = 'Comment=' + str(item['news_hot'])
            file.write(hot)
            file.write('\r\n')
        if item['news_title']:
            title = '标题=' + item['news_title']
            file.write(title)
            file.write('\r\n')
        if item['news_body']:
            body = '正文='
            file.write(body)
            body = item['news_body']
            for each in body:
                file.write(each)
            file.write('\r\n')
        return item
