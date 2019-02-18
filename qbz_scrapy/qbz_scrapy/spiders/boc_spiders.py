# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/9/19 9:54
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TestSpider(scrapy.Spider):
    name = "boc"

    def start_requests(self):
        urls = ["http://www.boc.cn/sourcedb/operations/406/522/526/", ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lis = response.xpath('//tr//td')
        for li in lis:
            print li.xpath("text()").extract()[0].strip().decode("utf-8")
