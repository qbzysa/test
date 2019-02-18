# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/2/11 11:15
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.selector import Selector
from qbz_scrapy.items import LogoItem
from scrapy.linkextractors import LinkExtractor


class LogoSpider(CrawlSpider): #CrawlSpider用来遍布抓取，通过rules来查找所有符合的URL来爬去信息

    name = "carlogo"
    allowed_domains = ["pcauto.com.cn"]
    start_urls = ["http://www.pcauto.com.cn/zt/chebiao/"]
    rules = (
        Rule(LinkExtractor(allow=(r'http://www.pcauto.com.cn/zt/chebiao/.*?/$')), follow=True, callback='parse_page'),
        )

    def parse_page(self, response):
        sel = Selector(response)
        item = LogoItem()
        item['country'] = ''.join(sel.xpath('//div[@class="th"]/span[@class="mark"]/a/text()').extract())
        item['carname'] = sel.xpath('//div[@class="dTxt"]/i[@class="iTit"]/a/text()').extract()
        item['imageurl'] = sel.xpath('//div[@class="dPic"]/i[@class="iPic"]/a/img/@src').extract()
        return item