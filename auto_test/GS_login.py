# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/8 9:16
from selenium import webdriver


class GlideSky(object):

    def __init__(self):
        self.driver = self.get_driver()
        self.cookies = self.get_cookies()

    def get_driver(self):
        """
        selenium获取登录配置
        :return:
        """
        # selenium+谷歌浏览器无界面设置
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.set_headless()
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # selenium+火狐浏览器无界面设置
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_headless()
        driver = webdriver.Firefox(firefox_options=firefox_options)


        driver.implicitly_wait(30)
        driver.maximize_window()
        base_url = "http://glidedsky.com/login"
        driver.get(base_url)
        return driver

    def get_cookies(self):
        """
        模拟登录github,返回cookies
        :return:
        """
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("2541183419@qq.com")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("pansafe123456")
        self.driver.find_element_by_css_selector(".btn.btn-primary").click()
        cookies = self.driver.get_cookies()
        ck = {}
        for cookie in cookies:
            key = cookie['name']
            ck[key] = cookie['value']
        return ck


if __name__ == "__main__":
    gs = GlideSky()
    print (gs.cookies)
