#!/usr/local/bin python
# -*- coding: utf8 -*-

'''scrapy 测试rule.

日期：2016-04-27
作者：Fan Yitian
'''

# 标准库
import sys

# 第三方库
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings  
import pymysql

# 应用程序自有库
from blogs import model
from blogs.spiders.common import CommonSpider


reload(sys)
sys.setdefaultencoding('utf-8')

# rule = {
# 	'name': 'test',
# 	'allow_domains': "51cto.com",
# 	'start_urls': "http://lmzj26.blog.51cto.com/all/1081403/page/1",
# 	'next_page': "//div[@class='blogRight']//div[@id='page']//a",
# 	'allow_url': "/\d+/\d+",
# 	'extract_from': "//div[@class='blogRight']",
# 	'title_xpath': "//div[@class='blogRight']//div[@class='showHead']//div[@class='showTitle']/text()[last()]",
# 	'body_xpath': "//div[@class='blogRight']//div[@class='showContent']//text()",
# 	'publish_time_xpath': "//div[@class='blogRight']//div[@class='showHead']//span[@class='artTime']/text()",
# 	'author_xpath': "//div[@class='blogLeft']//h2//strong/text()",
# }
rule = {
	'name': '54chen',
	'allow_domains': '54chen.com',
	'start_urls': 'http://2014.54chen.com/',
	'next_page': "//div[@id='content']//div[@class='pagination']//a[contains(@href, 'posts')]",
	'allow_url': '\/blog\/\d+\/\d+\/\d+',
	'extract_from': "//div[@id='content']",
	'title_xpath': "//article//header//h1//text()",
	'body_xpath': "//article//div[@class='entry-content']//text()",
	'publish_time_xpath': "//div[@class='x-content']//span[@class='x-smartdate']//text()",
	'author_xpath': "//div[@class='x-content']//p//a[contains(@href, 'user')]//text()",
}


# get insert sql.
keys = []
values = []
for key, value in rule.items():
	keys.append(key)
	values.append(pymysql.escape_string(value))

sql = "insert into `rules`(`%s`) values('%s')" % ("`,`".join(keys), "','".join(values))
print(sql)
# exit()


settings = Settings()

# crawl settings
settings.set("ITEM_PIPELINES", {
   'blogs.pipelines.TestForPipeline': 300
})
settings.set("LOG_LEVEL", "INFO")
settings.set("LOG_FILE", "log/run_test.log")


process = CrawlerProcess(settings)
process.crawl(CommonSpider, rule)
process.start()