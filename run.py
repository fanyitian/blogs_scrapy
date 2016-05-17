#!/usr/local/bin python
# -*- coding: utf8 -*-

'''scrapy 全量爬取blog

@date：2016-04-27
@author：Fan Yitian
@version: 0.1.1
@brief: 
	命令行接收rule_id参数，根据rule来爬取blog
	`python run.py 1 2 3`
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

rule_ids = []
# 检查命令行参数
for i in range(1, len(sys.argv)):
	rule_ids.append(int(sys.argv[i]))
if not rule_ids:
	print('rules id is empty, please input the integer argv.\nlike: `python run.py 1 22 33`')
	exit(1)


# crawl settings
settings = get_project_settings()
settings.set("ITEM_PIPELINES", {
   'blogs.pipelines.FilterPipeline': 100,
   'blogs.pipelines.DuplicatesPipeline': 200,
   'blogs.pipelines.DdPipeline': 300,
})
logName = "log/run_%s.log" % (time.strftime("%F"))
settings.set("LOG_FILE", logName)


process = CrawlerProcess(settings)

# 获取rules
rules = model.getRulesByRuleIds(rule_ids)
for rule in rules:
	process.crawl(CommonSpider, rule)
process.start()


