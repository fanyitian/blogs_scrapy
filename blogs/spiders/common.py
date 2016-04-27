#!/usr/local/bin python
# -*- coding: utf8 -*-

'''通用Spider

日期：2016-04-27
作者：Fan Yitian
'''

# 标准库
from urlparse import urlparse

# 第三方库
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 应用程序自有库
from blogs.items import BlogsItem


class CommonSpider(CrawlSpider):
    name = 'common'
    download_delay = 1

    def __init__(self, rule):
        self.rule = rule
        self.name = rule['name']
        self.allowed_domains = rule['allow_domains'].split(",")
        self.start_urls = rule['start_urls'].split(",")

        rule_list = []
        # 添加`下一页`规则
        if rule['next_page']:
            rule_list.append(Rule(LinkExtractor(restrict_xpaths = rule['next_page'])))

        # 添加文章链接规则
        rule_list.append(Rule(LinkExtractor(
            allow = [rule['allow_url']], 
            restrict_xpaths = [rule['extract_from'] if rule['extract_from'] else '']),
            callback = 'parse_item'))

        self.rules = tuple(rule_list)
        super(CommonSpider, self).__init__()


    def parse_item(self, response):
        self.logger.info("download article: %s" % (response.url))

        i = BlogsItem()
        i['url'] = response.url

        title = response.xpath(self.rule['title_xpath']).extract()
        i['title'] = title[0].strip() if title else ""

        body = response.xpath(self.rule['body_xpath']).extract()
        tmpBody = []
        for row in body:
            if not row.strip():
                continue;
            tmpBody.append(row)
        i['body'] = '\n'.join(tmpBody)


        author = response.xpath(self.rule['author_xpath']).extract()
        i['author'] = author[0] if author else urlparse(response.url).hostname       # 若未解析到author, 则使用host

        publish_time = response.xpath(self.rule['publish_time_xpath']).extract()
        pb_time = publish_time[0] if publish_time else response.url   # 若未匹配到时间，则尝试使用url解析
        pb_time = pb_time.replace(u"年", '-').replace(u"月","-").replace("/","-")

        pattern = re.compile(r'(\d{2,4}-\d{1,2}-\d{1,2})')
        pattern_str = pattern.search(pb_time)
        if pattern_str:
            i['publish_time'] = pattern_str.group(0)
        else:
            i['publish_time'] = "0000-00-00"

        return i
    