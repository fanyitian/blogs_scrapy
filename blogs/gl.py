#!/usr/local/bin python
# -*- coding: utf8 -*-

'''全局变量

日期：2016-04-27
作者：Fan Yitian
'''

# 标准库

# 第三方库
import redis 
from scrapy.utils.project import get_project_settings  

# 应用程序自有库
import mysql



# mysql
db = None

# redis
r = None


def connectDB():
	global db
	if db is None:
		settings = get_project_settings()
		db = mysql.MySQL({
				'host': settings.get('MYSQL_HOST'), 
				'port': settings.get('MYSQL_PORT'),
				'user': settings.get('MYSQL_USER'),
				'passwd': settings.get('MYSQL_PASSWD'),
				'db': settings.get('MYSQL_DBNAME'),
				})
	return db

def connectRedis():
	global r
	if r is None:
		settings = get_project_settings()
		r = redis.StrictRedis(host = settings.get('REDIS_HOST'), port = settings.get('REDIS_PORT'))
	return r


def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()   
        m.update(str)
        return m.hexdigest()
    else:
        return ''

connectDB()
connectRedis()
