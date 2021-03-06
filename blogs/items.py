# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogsItem(scrapy.Item):
    # define the fields for your item here like:
    author_id = scrapy.Field()
    rule_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    publish_time = scrapy.Field()
    pass
