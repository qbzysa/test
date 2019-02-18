# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from settings import PROXY_LIST


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, user_agent='Scrapy'):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings['USER_AGENT_LIST'])

    def process_request(self, request, spider):
        print "**************************" + random.choice(self.user_agent)
        request.headers.setdefault('User-Agent', random.choice(self.user_agent))


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == 'carlogo':
            proxy = random.choice(PROXY_LIST)
            print proxy
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
