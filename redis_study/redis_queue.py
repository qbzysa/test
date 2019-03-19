# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/10/25 13:59
import redis
pool = redis.ConnectionPool(host='192.168.16.230',
                            password='123456',
                            port=6379)


class RedisQueue(object):
    def __init__(self, name, namespace='queue'):
        self.__db = redis.Redis(connection_pool=pool)
        self.key = '%s:%s' % (namespace, name)

    # 返回队列里面list内元素的数量
    def qsize(self):
        return self.__db.llen(self.key)

    # 添加新元素到队列最右方
    def put(self, item):
        self.__db.rpush(self.key, item)

    # 返回队列第一个元素，如果为空则等待至有元素被加入队列（超时时间阈值为timeout，如果为None则一直等待）
    def get_wait(self, timeout=None):
        item = self.__db.blpop(self.key, timeout=timeout)
        return item

    # 直接返回队列第一个元素，如果队列为空返回的是None
    def get_nowait(self):
        item = self.__db.lpop(self.key)
        return item
