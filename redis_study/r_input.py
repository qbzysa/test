# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/10/25 13:59
from redis_queue import RedisQueue
import time

q = RedisQueue('rq')  # 新建队列名为rq
for i in range(5):
    q.put(i)
    print "input.py: data {} enqueue {}".format(i, time.strftime("%c"))
    time.sleep(1)