#!/usr/local/bin python
# -*- coding: utf8 -*-

'''scrapy 测试rule.

日期：2016-04-27
作者：Fan Yitian
'''

# 标准库
import sys
import time

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
   'blogs.pipelines.TestForPipeline': 300
})
logName = "log/run_test_%s.log" % (time.strftime("%F"))
settings.set("LOG_LEVEL", 'INFO')
settings.set("LOG_FILE", logName)


# 检查命令行参数
ruleId = int(sys.argv[1])
if not ruleId:
	print('rule id is empty, please input the integer argv.\nlike: `python run_test.py 1`')
	exit(1)


# 获取rules
rule = model.getRuleById(ruleId)
if rule is None:
	print('can\'t not find rule by rule_id:%s' % ruleId)
	exit(1)
rule.pop('next_page')


process = CrawlerProcess(settings)
process.crawl(CommonSpider, rule)
process.start()