# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/8/24 9:27
import scrapy
from auto_test.GS_login import GlideSky
import re
import os
import time

# CSS反爬
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/66.0.3359.139 Safari/537.36 "
    }


class CssSpider(scrapy.Spider):
    name = "css_spider"
    gs = GlideSky()
    data = 0

    def start_requests(self):
        try:
            if os.path.exists('css_data.txt'):
                os.remove('css_data.txt')
            for i in range(1, 1001):
                url = "http://glidedsky.com/level/web/crawler-css-puzzle-1?page=%s" % i
                yield scrapy.Request(url=url, callback=self.parse, cookies=self.gs.cookies)
                time.sleep(2)
        finally:   
            time.sleep(200)
            self.gs.driver.close()

    def parse(self, response):
        # 获取css
        css_data = response.xpath('/html/head/style/text()').extract()[0].strip().split('\n')
        # 处理css,获取有用的信息
        enable, disable = self.Processing_CSS(css_data)
        elements = response.xpath('..//div[@class="col-md-1"]')
        # 将html中的数字转换成web中显示的数字
        for element in elements:
            if element.root.tag == 'div':
                text = element.extract()
                result = re.findall(r'class="(.*?)">(.*?)<', text, flags=re.S)
                lis1 = []
                lis2 = []
                for k in range(1, len(result)):
                    if result[k][0] not in disable:
                        if len(result) >= 3 and result[k][1] != '':
                            num_1 = enable.get(result[k][0], '0')
                            num = k + int(num_1)
                            lis1.append(num)
                            lis2.append(result[k][1])
                        else:
                            if result[k][1] == '':
                                name = enable.get(result[k][0])
                                self.data += int(name)
                                with open('css_data.txt', 'a') as f:
                                    f.write(name+'\n')
                if len(lis1):
                    st = ''
                    for m in sorted(lis1):
                        for n in range(len(lis1)):
                            if lis1[n] == m:
                                st = st + str(lis2[n])
                            continue
                    self.data += int(st)
                    with open('css_data.txt', 'a') as f:
                        f.write(st + '\n')
        print(self.data)

    def Processing_CSS(self, css_data):
        """
        对css_data进行处理
        :css_data:  css数据列表
        :return:
        """
        css_dict = {}
        disable = []
        for i in css_data:
            # 显示css属性
            if '{ left:' in i:
                req = re.findall('\.(.*)? { left:(.*?)\s\}', i)[0]
                if req[0] in css_dict.keys():
                    css_dict[req[0]]['left'] = req[1].split('em')[0]
                else:
                    css_dict[req[0]] = req[1].split('em')[0]
            elif 'before' in i:
                req = re.findall('\.(.*)?:before { content:"(.*?)" }', i)[0]
                css_dict[req[0]] = req[1]
            # 不显示css属性
            if 'opacity:0' in i:
                req = re.findall('\.(.*)? {', i)[0]
                disable.append(req)
        return css_dict, disable
