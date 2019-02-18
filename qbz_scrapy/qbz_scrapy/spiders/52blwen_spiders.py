# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/8/21 13:38
import scrapy
import sys
import re
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')


class TestSpider(scrapy.Spider):
    name = "52blwen"
    a = ""

    def start_requests(self):
        urls = ["http://www.52blwen.com/xiandaidushi/2018/0708/27829.html",]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lis = response.xpath("//div/div/div/div")
        for li in lis:
            try:
                name = li.xpath("text()").extract()[0].strip().decode("utf-8")
                if name and "点击：" not in name and "字体:[" not in name:
                    self.a += name
            except:
                pass
        print self.a
