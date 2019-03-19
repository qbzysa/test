# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/12/6 15:40
import requests
import sys
import os
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')
save_dir = "E:\\data\\html"


def get_html(url, number):
    """
    :param url: 网站url
    :param number:  序号
    :return:
    """
    file_name = str(number)+".html"
    print url
    res = requests.get(url)
    res.encoding = 'utf-8'
    with open(os.path.join(save_dir, file_name), 'w+') as f:
        f.write(res.text)


if __name__ == "__main__":
    infos = pd.read_excel("URL.xlsx", header=None)
    num = 1
    for i in infos[0]:
        get_html(i, num)
        num += 1