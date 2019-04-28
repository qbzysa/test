# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/8/24 9:27
import scrapy
from auto_test.GS_login import GlideSky
import re
import requests
from change_font.get_font import get_font
import os
import time

headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/66.0.3359.139 Safari/537.36 "
    }


class TestSpider(scrapy.Spider):
    name = "test"
    gs = GlideSky()
    data = []
    num_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
                '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

    def start_requests(self):
        for i in range(1, 1001):
            url = "http://glidedsky.com/level/web/crawler-font-puzzle-1?page=%s" % i
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.gs.cookies)
            time.sleep(2)
            

    def parse(self, response):
        # 获取字体文件的url
        woff_url = re.search(r"url\(\"(.*\.woff)\"\)", response.text).group(1)
        response_woff = requests.get(woff_url, headers=headers, verify=False).content
        woff_path = os.path.join('E:/testpy3/change_font', woff_url.split('/')[-1]).replace('\\', '/')

        with open(woff_path, 'wb') as f:
            f.write(response_woff)
        # 当前字体跟数字的关系
        font_dict = get_font(woff_path)
        lis = response.xpath('..//div[@class="col-md-1"]')

        for li in lis:
            html_name = li.xpath("text()").extract()[0].strip()
            print('h', html_name)
            hundred = font_dict.get(self.num_dict.get(html_name[0]))
            ten = font_dict.get(self.num_dict.get(html_name[1]))
            one = font_dict.get(self.num_dict.get(html_name[2]))

            name = int(hundred)*100+10*int(ten)+int(one)
            print('n', name)
            self.data.append(int(name))
        print(sum(self.data))
        print(len(self.data))
