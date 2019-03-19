# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/25 8:34
import urllib
import httplib


# GET请求
def get(id):
    requrl = "http://127.0.0.1:5000/%s" % id
    headerdata = {"Host":"127.0.0.1"}
    conn = httplib.HTTPConnection("127.0.0.1", "5000")
    conn.request(method="GET", url=requrl, headers=headerdata)
    response = conn.getresponse()
    res = response.read()
    print res
    conn.close


def get_all():
    requrl = "http://127.0.0.1:5000/all"
    headerdata = {"Host": "127.0.0.1"}
    conn = httplib.HTTPConnection("127.0.0.1", "5000")
    conn.request(method="GET", url=requrl, headers=headerdata)
    response = conn.getresponse()
    res = response.read()
    print res
    conn.close


# PUT请求
def create(id, name):
    test_data = {"id": id, "name": name}
    test_data_urlencode = urllib.urlencode(test_data)
    requrl = "http://127.0.0.1:5000/create"
    headerdata = {"Host": "127.0.0.1"}
    conn = httplib.HTTPConnection("127.0.0.1", "5000")
    conn.request(method="PUT", url=requrl, body=test_data_urlencode, headers=headerdata)
    response = conn.getresponse()
    res = response.read()
    print res
    conn.close


# POST请求
def update(id, name):
    test_data = {"id": id, "name": name}
    test_data_urlencode = urllib.urlencode(test_data)
    requrl = "http://127.0.0.1:5000/update"
    headerdata = {"Host":"127.0.0.1"}
    conn = httplib.HTTPConnection("127.0.0.1", "5000")
    conn.request(method="POST", url=requrl, body=test_data_urlencode, headers=headerdata)
    response = conn.getresponse()
    res = response.read()
    print res
    conn.close()


# DELETE请求
def delete(id):
    requrl = "http://127.0.0.1:5000/delete/%s" % id
    headerdata = {"Host": "127.0.0.1"}
    conn = httplib.HTTPConnection("127.0.0.1", "5000")
    conn.request(method="DELETE", url=requrl, headers=headerdata)
    response = conn.getresponse()
    res = response.read()
    print res
    conn.close()


if __name__ == "__main__":
      update(id=3, name="ooo")