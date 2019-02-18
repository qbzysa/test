# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/8/13 17:42
import scrapy
import sys
import re
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')


class CtripCitySpider(scrapy.Spider):
    name = "ctrip_city"

    def start_requests(self):
        urls = ['http://hotels.ctrip.com/domestic-city-hotel.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lis = response.xpath("//dd/a")
        for li in lis:
            city_name = li.xpath("@title").extract()[0].decode("utf-8")[:-2]
            test = li.xpath("@href").extract()[0].split("/")[-1]
            city_id = re.findall(r"\d+", test)[0]
            db = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='test', charset="utf8")
            cursor = db.cursor()
            insert_sql = '''INSERT INTO xiecheng_city(city_id,city_name) values ('%s', '%s');''' % (city_id, city_name)
            print(insert_sql)
            try:
                cursor.execute(insert_sql)
                db.commit()
            except:
                db.rollback()
            db.close()