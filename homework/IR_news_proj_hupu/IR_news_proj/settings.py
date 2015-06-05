# -*- coding: utf-8 -*-

# Scrapy settings for IR_news_proj project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'IR_news_proj'

SPIDER_MODULES = ['IR_news_proj.spiders']
NEWSPIDER_MODULE = 'IR_news_proj.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'IR_news_proj (+http://www.yourdomain.com)'


CLOSESPIDER_ITEMCOUNT = 10000
DOWNLOAD_TIMEOUT = 300
DOWNLOAD_DELAY = 0.25

ITEM_PIPELINES = ['IR_news_proj.pipelines.IrNewsProjPipeline']