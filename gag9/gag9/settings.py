# -*- coding: utf-8 -*-

# Scrapy settings for gag9 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gag9'

SPIDER_MODULES = ['gag9.spiders']
NEWSPIDER_MODULE = 'gag9.spiders'

DUPEFILTER_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gag9 (+http://www.yourdomain.com)'


ITEM_PIPELINES = ['gag9.pipelines.GagPipeline', ]
