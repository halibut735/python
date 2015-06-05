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



COOKIES_ENABLED = True
COOKIES_DEBUG = True
RETRY_ENABLED = False
CONCURRENT_ITEMS = 50
DOWNLOAD_TIMEOUT = 100
CLOSESPIDER_ITEMCOUNT = 40000

ITEM_PIPELINES = ['IR_news_proj.pipelines.IrNewsProjPipeline']