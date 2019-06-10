import scrapy
import sys
import requests
import re
import urllib
import time
reload(sys)
sys.setdefaultencoding('utf-8')


class FbmSpider(scrapy.Spider):
    name = "fbm"

    def start_requests(self):
        # urls = []
        # for i in range(1, 76):
        #    base_url = "http://www.gyxww.cn/fbm/2Wyxxy/show-14-{}.html".format(i)
        #    urls.append(base_url)
        # for url in urls:
        #    yield scrapy.Request(url=url, callback=self.parse)
        #    time.sleep(10)

        yield scrapy.Request(url="http://www.gyxww.cn/c/2Wyxxy/show-14-17.html", callback=self.parse)

    def parse(self, response):
        
        # 获取加密的js_url
        info_urls = re.findall('<script src="(.*)"', response.text)
        for url in info_urls:
            if 'http://fabu.fabumao.com.cn/index/contact/icard' in url:
                js_url = url
                break
        print js_url
        # 解密
        req = requests.get(js_url)
        data = req.text.split(';')[0]
        print data
        info = re.search("var str = '(.*)'", str(data)).group(1).split(',')[::-1]
        print info
        code = ''
        for i in info[1:]:
           code += '%' + i
        print urllib.unquote(code)

