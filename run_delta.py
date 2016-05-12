#!/usr/local/bin python
# -*- coding: utf8 -*-

'''scrapy 增量blog

@date：2016-05-12
@author：Fan Yitian
@version: 0.0.1
@brief: 
'''

# 标准库
import sys
import time
import os

# 第三方库
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings  

# 应用程序自有库
from blogs import model
from blogs.spiders.common import CommonSpider

reload(sys)
sys.setdefaultencoding('utf-8')

# crawl settings
settings = get_project_settings()
settings.set("ITEM_PIPELINES", {
   'blogs.pipelines.FilterPipeline': 100,
   'blogs.pipelines.DuplicatesPipeline': 200,
   'blogs.pipelines.DdPipeline': 300,
})

logName = "log/run_delta_%s.log" % (time.strftime("%F"))
settings.set("LOG_LEVEL", 'INFO')
settings.set("LOG_FILE", logName)

process = CrawlerProcess(settings)

# 获取rules
rules = model.getEnableRules()
for rule in rules:
	process.crawl(CommonSpider, rule)
process.start()