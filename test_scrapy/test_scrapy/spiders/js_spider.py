# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/8/24 9:27
import scrapy
from auto_test.GS_login import GlideSky
import math
import requests
import hashlib
import time
import os

# JS反爬
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/66.0.3359.139 Safari/537.36 "
    }


class JsSpider(scrapy.Spider):
    name = "js_spider"
    gs = GlideSky()
    data = []

    def start_requests(self):
        #if os.path.exists('js_data.txt'):
        #    os.remove('js_data.txt')
        for i in range(1, 1001):
            url = "http://glidedsky.com/level/web/crawler-javascript-obfuscation-1?page=%s" % i
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.gs.cookies)
            time.sleep(2)
        time.sleep(5)
        self.gs.driver.close()

    def parse(self, response):
        # 模拟js加密
        p = response.css('.container::attr(p)').extract()[0]
        t0 = int(response.css('.container::attr(t)').extract()[0])
        t = math.floor((t0-99)/99)
        tmp = 'Xr0Z-javascript-obfuscation-1' + str(t)
        sign = hashlib.sha1(tmp.encode("utf-8")).hexdigest()
        # 访问data_url,获取数据
        data_url = 'http://glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?page=%s&t=%s&sign=%s' % (p, t, sign)
        req = requests.get(data_url, cookies=self.gs.cookies)
        print(req.json())
        print(req.json()['items'])
        info = req.json()['items']
        self.data += list(info)
        print(sum(self.data))
        with open('js_data.txt', 'a') as f:
            f.write(str(list(info)) + '\n')
