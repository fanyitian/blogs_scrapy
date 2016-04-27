#!/usr/local/bin python
# -*- coding: utf8 -*-

'''scrapy 全量爬取blog

日期：2016-04-27
作者：Fan Yitian
'''

# 标准库
import sys

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


process = CrawlerProcess(settings)

# 获取rules
rules = model.getRules()
for rule in rules:
	process.crawl(CommonSpider, rule)
process.start()


