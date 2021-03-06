#!/usr/local/bin python
# -*- coding: utf8 -*-

''' item pipelines

日期：2016-04-27
作者：Fan Yitian
'''

# 标准库
import time
import pprint

# 第三方库
from scrapy.exceptions import DropItem
import pymysql

# 应用程序自有库
import gl
import mysql



REDIS_PRE = 'blogs_'

# 过滤
class FilterPipeline(object):
    def process_item(self, item, spider):
        if item['title'] == "":
            raise DropItem("item title is empty. in %s" % (item['url']))
        else:
            return item

# 去重
class DuplicatesPipeline(object):
	def process_item(self, item, spider):
		urlExist = self._isExistUrl(item['url'], item['rule_id'])
		if urlExist:
			raise DropItem("Duplicate item found: %s " % item['url'])
		else:
			urlmd5 = gl.md5(item['url'])
			key = REDIS_PRE + 'ruleid:%s:url:%s' % (item['rule_id'], urlmd5)
			gl.r.set(key, 1)
			return item

	def _isExistUrl(self, url, ruleId):
		urlmd5 = gl.md5(url)
		# 先检查redis，再检查db
		key = REDIS_PRE + 'ruleid:%s:url:%s' % (ruleId, urlmd5)
		if gl.r.exists(key):
			return True

		sql = "select `id` from `articles` where `urlmd5` = '%s'" % (urlmd5)
		gl.db.query(sql)
		res = gl.db.fetchOneRow()
		if res:
			return True

		return False


# 存到数据库
class DdPipeline(object):
    def process_item(self, item, spider):
    	print("DdPipeline: %s" % (item['url']))

    	author_id = item['author_id']
    	rule_id = item['rule_id']
    	urlmd5 = gl.md5(item['url'])
    	title = pymysql.escape_string(item['title'].encode('utf-8'))
    	body = pymysql.escape_string(item['body'].encode('utf-8'))
    	publish_time = item['publish_time'].encode('utf-8')
    	create_time = time.strftime("%F %T")

    	sql = "insert into `articles`(`author_id`, `rule_id`, `urlmd5`, `url`, `title`, `body`, `publish_time`, `create_time`) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
    	par = (author_id, rule_id, urlmd5, item['url'], title, body, publish_time, create_time)
    	sql %= (par)
    	r = gl.db.insert(sql)
    	# 插入失败，在redis里删除key
    	if not r:
    		key = REDIS_PRE + 'url:%s' % urlmd5
    		gl.r.delete(key)

    	return item

# 测试pipline。仅爬取一次
class TestForPipeline(object):
	def process_item(self, item, spider):
		# print("item: ......")
		# pprint.pprint(item)

		loginfo = []
		loginfo.append('--------------- item --------------')
		loginfo.append("[url]: %s" % item['url'])
		loginfo.append("[pub_time]: %s" % item['publish_time'])
		loginfo.append("[title]: %s" % (item['title']))
		loginfo.append("[body]: %s ......\n" % (item['body'][:100]))

		spider.logger.info("test_process_item: %s" % (',\t'.join(loginfo)))
		print("\n".join(loginfo))

		spider.close_down = True
		return item
		

		