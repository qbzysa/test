# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/7 16:53
import scrapy
import time
from auto_test.github_login import GitHub
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class GitHubSpider(scrapy.Spider):
    name = 'github'

    def start_requests(self):
        gb = GitHub()
        # 获取所有需要爬虫的url
        html = gb.html
        # 获取登录后的cookies
        cookies = gb.cookies
        # 获取selenium的driver
        if os.path.exists('user.txt'):
            os.remove('user.txt')
        for url in html:
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)
            time.sleep(2)
        gb.driver.close()

    def parse(self, response):
        email = ""
        s_usename = response.xpath("//*[@class='p-name vcard-fullname d-block overflow-hidden']").\
            xpath("text()").extract()
        s_email = response.xpath("//*[@class='u-email']").xpath("text()").extract()
        if s_usename:
            try:
                username = s_usename[0].strip().decode("utf-8")
            except:
                username = s_usename[0].strip()
            if s_email:
                try:
                    email = s_email[0].strip().decode("utf-8")
                except:
                    email = s_email[0].strip()

            with open('user.txt', 'a') as f:
                f.write(username)
                f.write('\t')
                f.write(email)
                f.write('\n')












