# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/11/6 9:32
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from qbz_scrapy.items import MaoyanItem
import MySQLdb


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    # allowed_domains = ['maoyan.com']
    pagelist = [7, 6, 1, 2, 4]

    def clear_data(self):
        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                               db='test', charset='utf8')
        # 建立游标对象
        cursor = conn.cursor()
        cursor.execute('truncate table maoyan')
        cursor.close()
        conn.commit()
        conn.close()

    def start_requests(self):
        self.clear_data()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
        }
        for i in self.pagelist:
            self.url = 'http://maoyan.com/board/{page}'.format(page=i)
            yield Request(self.url, callback=self.parse, headers=headers)

    def parse(self, response):
        item = MaoyanItem()
        selector = Selector(response)
        active = selector.xpath('//ul[@class="navbar"]/li/a[@class="active"]/text()').extract()
        tops = selector.xpath('//dd/i/text()').extract()
        movies = selector.xpath('//div[@class="movie-item-info"]')
        for i, content in enumerate(movies):
            title = content.xpath('p[@class="name"]/a/text()').extract()
            star = content.xpath('p[2]/text()').extract()
            releasetime = content.xpath('p[3]/text()').extract()

            item['top'] = active[-1] + '第' + tops[i]
            item['title'] = title[0]
            item['star'] = star[0].replace(' ', '').replace('\n', '')
            if releasetime:
                item['releasetime'] = releasetime[0].replace(' ', '').replace('\n', '')
            else:
                item['releasetime'] = ''
            yield item

