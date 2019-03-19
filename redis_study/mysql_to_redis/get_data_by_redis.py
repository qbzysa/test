# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/11/29 10:19
import redis
import configparser

config = configparser.ConfigParser()
config.read('./dbconfig.conf')
host = config['REDIS']['host']
port = config['REDIS']['port']
db = config['REDIS']['db']
password = config['REDIS']['password']
pool = redis.ConnectionPool(host=host,
                            password=password,
                            port=int(port),
                            db=int(db))


class Redis_data(object):

    def __init__(self):
        self.__rd = redis.Redis(connection_pool=pool)

    ##################string################
    def add_string_redis(self, data):
        for i in data:
            key ="%s:%s:%s"% ('test','xiecheng_city', i.get('city_id'))
            value = i.get('city_name')
            if key and value:
                self.__rd.set(key, value)
            else:
                pass

    ##################hash######################
    def add_hash_redis(self, data):
        key = 'test:xiecheng_city_hash'
        info_dict = {}
        for i in data:
            info_dict[i.get('city_id')] = i.get('city_name')
        self.__rd.hmset(key, info_dict)

    ##################list######################
    def add_list_redis(self, data):
        key = 'test:xiecheng_city_list'
        self.__rd.lpush(key, data)

    ####################set####################
    def add_set_redis(self, data):
        key = 'test:xiecheng_city_set'
        for i in data:
            self.__rd.sadd(key, i)

    def get_string_redis(self, city_id):
        return self.__rd.get(city_id)

    def get_hash_redis(self):
        key = 'test:xiecheng_city_hash'
        return self.__rd.hgetall(key)

    def get_list_redis(self):
        key = 'test:xiecheng_city_list'
        return self.__rd.lpop(key)

    def get_set_redis(self):
        key = 'test:xiecheng_city_set'
        return self.__rd.smembers(key)




