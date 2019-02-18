# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QbzScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MaoyanItem(scrapy.Item):
    top = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    releasetime = scrapy.Field()


class KuaidiItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()


class LogoItem(scrapy.Item):
    country = scrapy.Field()
    carname = scrapy.Field()
    imageurl = scrapy.Field()
