# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/9 9:12
from scrapy import cmdline
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # cmdline.execute("scrapy crawl github".split())
    #cmdline.execute("scrapy crawl maoyan".split())
    # cmdline.execute("scrapy crawl kuaidi100".split())
    cmdline.execute("scrapy crawl carlogo".split())
