# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/25 14:08
import scrapy
import sys
import MySQLdb
from qbz_scrapy.items import KuaidiItem

reload(sys)
sys.setdefaultencoding('utf-8')


class TestSpider(scrapy.Spider):
    name = "kuaidi100"

    def clear_data(self):
        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                                    db='test', charset='utf-8')
        # 建立游标对象
        cursor = conn.cursor()
        cursor.execute('truncate table kuaidi')
        cursor.close()
        conn.commit()
        conn.close()

    def start_requests(self):
        url = "https://www.kuaidi100.com/all"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = KuaidiItem()
        print response.text
        lis = response.xpath('..//div[@class="w960"]//div//dl//dd//a')
        for one in lis:
            try:
                html_url = one.xpath("@href").extract()[0].strip().decode("utf-8")
                if "all" in html_url:
                    name = one.xpath("text()").extract()[0].strip().decode("utf-8")
                    item['url'] = html_url
                    item['name'] = name
                    item['type'] = str(html_url).split('/')[-1].split('.')[0]
                    yield item
            except Exception as e:
                print e




