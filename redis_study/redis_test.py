# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/10/25 9:02
import redis
pool = redis.ConnectionPool(host='192.168.16.230',
                            password='123456',
                            port=6379)


# 从redis连接池中获取一个连接
def get_conn():
    conn = redis.Redis(connection_pool=pool)
    return conn


if __name__ == "__main__":
    r = get_conn()
    r.set(name="k1", value="aaa", ex=60)
    res = r.get(name="k1")
    print(res)
#     r.hset('test', 'name', 'qbz')
#     print r.hget('test', 'name')
#
#     info = {'name': 'ysa',
#             'age': 24,
#             'sex': 'M'}
#     r.hmset('test1', info)
#     print r.hgetall('test1')
#
#     print r.hmget('test1', 'name', 'age', 'sex')
#     print r.hlen('test1')
#     print r.hkeys('test1')
#     print r.hvals('test1')