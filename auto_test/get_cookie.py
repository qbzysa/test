# -*- coding: utf-8 -*-
# __author__:'Administrator'
import requests

def getCookie():
    url = "http://glidedsky.com/login"
    Hostreferer = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    # get方法中加入verify参数，并设为False
    # 根据url的实际情况对请求的类型以及传入的参数进行调整
    html = requests.get(url, headers=Hostreferer, verify=False, data={'email': '******', 'password':'*****'})
    # 获取cookie
    ck = {}
    if html.status_code == 200:
        for cookie in html.cookies:
            key = cookie.name
            value = cookie.value
            ck[key] = value
    return ck


if __name__ == '__main__':
    cookie = getCookie()
    print(cookie)
