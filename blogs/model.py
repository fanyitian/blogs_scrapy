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


def getRuleById(ruleId):
	"""根据id获取rule
	"""
	rules = getRulesByRuleIds([ruleId])
	return rules[0] if rules else None


def getRulesByRuleIds(ruleIds):
	"""根据rule_id获取rule

	Args:
		ruleIds list 		规则ids

	Returns:
		rule list.
	"""
	ruleIds = [str(i) for i in ruleIds]

	sql = "select id, author_id, allow_domains, start_urls, next_page, allow_url, extract_from, \
		title_xpath, body_xpath, publish_time_xpath from rules where id in (%s)" % (','.join(ruleIds))
	gl.db.query(sql)

	rules = [dict(id=row[0], author_id=row[1], allow_domains=row[2], start_urls=row[3], next_page=row[4], allow_url=row[5],\
		 extract_from=row[6], title_xpath=row[7], body_xpath=row[8], publish_time_xpath=row[9]) for row in gl.db.fetchAllRows()]
	return rules


def getEnableRules():
	"""获取需要爬取的rules, 不需要next_page
	"""
	sql = "select id, author_id, allow_domains, start_urls, allow_url, extract_from, \
		title_xpath, body_xpath, publish_time_xpath from rules where enable = 1"
	gl.db.query(sql)

	rules = [dict(id=row[0], author_id=row[1], allow_domains=row[2], start_urls=row[3], allow_url=row[4], extract_from=row[5], \
		title_xpath=row[6], body_xpath=row[7], publish_time_xpath=row[8]) for row in gl.db.fetchAllRows()]
	return rules
