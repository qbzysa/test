# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/8/24 9:27
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TestSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = []
        for i in range(1, 76):
            base_url = "http://m.shucong.com/books/lists?&page={}".format(i)
            urls.append(base_url)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        import demjson
        response_body = response.body.decode('utf-8')
        books_list = demjson.decode(response_body)
        info = {}
        for book in books_list:
            if len(book):
                info[book.get('articleid')] = book.get('articlename')
        print len(info)