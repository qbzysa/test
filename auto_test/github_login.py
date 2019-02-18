# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/8 9:16
from selenium import webdriver
import requests
import sys
import json
import time
reload(sys)
sys.setdefaultencoding('utf-8')


class GitHub(object):

    def __init__(self):
        self.html = self.get_user_htmlurl()
        self.driver = self.get_driver()
        self.cookies = self.get_cookies()

    def get_driver(self):
        """
        selenium获取登录配置
        :return:
        """
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.maximize_window()
        base_url = "https://github.com/login"
        driver.get(base_url)
        return driver

    def get_cookies(self):
        """
        模拟登录github,返回cookies
        :return:
        """
        self.driver.find_element_by_id("login_field").clear()
        self.driver.find_element_by_id("login_field").send_keys("******")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("******")
        self.driver.find_element_by_name('commit').click()
        cookies = self.driver.get_cookies()
        ck = {}
        for cookie in cookies:
            key = cookie['name']
            ck[key] = cookie['value']
        return ck

    def get_user_htmlurl(self):
        """
        获取github中国区用户的html_url
        :return:
        """
        html_urls = []
        page = 0
        while True:
            req = requests.get("https://api.github.com/search/users?q=location:china+type:user&page=%s" % page)
            if req.status_code != 200:
                break
            items = json.loads(req.text)['items']
            for item in items:
                html_urls.append(item.get("html_url"))
            page += 1
            time.sleep(5)
        return html_urls

