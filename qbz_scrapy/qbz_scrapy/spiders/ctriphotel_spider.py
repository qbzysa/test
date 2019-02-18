# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/8/13 17:42
import scrapy
import MySQLdb
import time
import random
import demjson
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class CtripHotelSpider(scrapy.Spider):
    name = "ctrip_hotel"
    count = 0

    def start_requests(self):
        urls = []
        db = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='test', charset="utf-8")
        cursor = db.cursor()
        select_sql = '''
        select city_id from xiecheng_city
        '''
        cursor.execute(select_sql)
        city_list = ["375"]
        for city in city_list:
            time.sleep(random.uniform(8, 9))
            self.city_id = city
            for i in range(1, 600):
                base_url = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx?StartTime={}&DepTime={}&cityId={}&page={}'.format(
                    '2018-08-16', '2018-08-17', self.city_id, i)
                urls.append(base_url)
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            response_body = response.body.decode('utf-8')
            hotel_list = demjson.decode(response_body)['hotelPositionJSON']
            for hotel in hotel_list:
                _hotel = Hotel(hotel['id'].encode('utf-8'),
                               hotel['name'].encode('utf-8'),
                               hotel['lat'].encode('utf-8'),
                               hotel['lon'].encode('utf-8'),
                               hotel['url'].encode('utf-8'),
                               hotel['img'].encode('utf-8'),
                               hotel['address'].encode('utf-8'),
                               hotel['score'].encode('utf-8'),
                               hotel['dpscore'].encode('utf-8'),
                               hotel['dpcount'].encode('utf-8'),
                               hotel['star'].encode('utf-8'),
                               hotel["stardesc"].encode('utf-8'),
                               hotel["shortName"].encode('utf-8'),
                               hotel['isSingleRec'].encode('utf-8'),
                               self.city_id)
                db = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='test', charset="utf8")
                cursor = db.cursor()
                insert_sql ='''
                INSERT INTO xiecheng_hotel (id,name,lat,lon,url,img,address,score,dpscore,dpcount,star,stardesc,shortName,isSingleRec,city_id) 
                SELECT {}, '{}', '{}','{}','{}','{}', '{}', '{}','{}','{}','{}', '{}', '{}',{},{} 
                from DUAL  
                where not exists(select id from xiecheng_hotel where id={});
                '''.format(_hotel.id,
                           _hotel.name,
                           _hotel.lat,
                           _hotel.lon,
                           _hotel.url,
                           _hotel.img,
                           _hotel.address,
                           _hotel.score,
                           _hotel.dpscore,
                           _hotel.dpcount,
                           _hotel.star,
                           _hotel.stardesc,
                           _hotel.shortName,
                           _hotel.isSingleRec,
                           _hotel.cityId,
                           _hotel.id)
                print(insert_sql)
                try:
                    cursor.execute(insert_sql)
                    db.commit()
                except:
                    db.rollback()
                db.close()
        except Exception as e:
            print("----------------------------------------------------")
            traceback.print_exc()


class Hotel(object):
    def __init__(self, id, name, lat, lon, url, img, address, score, dpscore,
                 dpcount, star, stardesc, shortName, isSingleRec, cityId):
        self.id = id  #酒店Id
        self.name = name  # 酒店名称
        self.lat = lat  # 纬度
        self.lon = lon  # 经度
        self.url = 'http://hotels.ctrip.com/'+url  # 详情链接
        self.img = 'http:'+img  # 酒店图片
        self.address = address  # 地址
        self.score = score  # 评分
        self.dpscore = dpscore  # 用户推荐占比 97%用户推荐
        self.dpcount = dpcount  # 点评人数
        self.star = star  # 星
        self.stardesc = stardesc  # 简介
        self.shortName = shortName #简称
        self.isSingleRec = isSingleRec
        self.cityId = cityId #城市ID
