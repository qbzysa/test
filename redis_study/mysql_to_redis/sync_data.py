# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/11/29 10:59
from get_data_by_mysql import get_data
from get_data_by_redis import Redis_data
import json

infos = get_data()
rd = Redis_data()
rd.add_string_redis(infos)
print rd.get_string_redis("test:xiecheng_city:100")
rd.add_set_redis(infos)
print rd.get_set_redis()
rd.add_list_redis(infos)
print rd.get_list_redis()
rd.add_hash_redis(infos)
print rd.get_hash_redis()
