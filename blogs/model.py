#!/usr/local/bin python
# -*- coding: utf8 -*-

'''数据模块

日期：2016-04-27
作者：Fan Yitian
'''

# 标准库

# 第三方库

# 应用程序自有库
import gl


def getRules():
	"""获取rules"""
	sql = "select id, name, allow_domains, start_urls, next_page, allow_url, extract_from, \
		title_xpath, body_xpath, publish_time_xpath, author_xpath from rules where enable = 1 "
	gl.db.query(sql)

	rules = [dict(id=row[0], name=row[1], allow_domains=row[2], start_urls=row[3], next_page=row[4], allow_url=row[5],\
		 extract_from=row[6], title_xpath=row[7], body_xpath=row[8], publish_time_xpath=row[9], author_xpath=row[10]) for row in gl.db.fetchAllRows()]
	return rules
