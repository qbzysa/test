# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/4/29 14:21
import scrapy
from auto_test.GS_login import GlideSky
import re
import os
import time
import random
# IP反爬
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/66.0.3359.139 Safari/537.36 "
    }


class IpSpider(scrapy.Spider):
    name = "ip_spider"
    gs = GlideSky()
    data = []
    proxy_list = ['http://148.70.254.52:52836',
                  'http://116.209.63.249:9999',
                  'http://180.175.90.14:8060']

    def start_requests(self):
        for i in range(1, 1001):
            url = "http://glidedsky.com/level/web/crawler-ip-block-1?page=%s" % i
            print(random.choice(self.proxy_list))
            yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': random.choice(self.proxy_list)}, cookies=self.gs.cookies)
            time.sleep(5)
        self.gs.driver.close()

    def parse(self, response):
        print(response)
        lis = response.xpath('..//div[@class="col-md-1"]')
        for li in lis:
            name = li.xpath('text()').extract()[0].strip()
            print(name)
            self.data.append(int(name))
        print(sum(self.data))
