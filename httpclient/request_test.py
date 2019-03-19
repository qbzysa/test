# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/24 15:11
import requests
import test


def get_all():
    reqs = requests.get("http://127.0.0.1:5000/all")
    print reqs.content


def get():
    reqs = requests.get("http://127.0.0.1:5000/1")
    print reqs.content


def create():
    data = {"id": "3", "name": "xt"}
    reqs = requests.put("http://127.0.0.1:5000/create", data=data)
    print reqs.content


def update():
    data = {"id":"3", "name": "twt"}
    reqs = requests.post("http://127.0.0.1:5000/update", data=data)
    print reqs.content


def delete():
    reqs = requests.delete("http://127.0.0.1:5000/delete/3")
    print reqs.content


if __name__ == "__main__":
    # get_all()
    # get()
    # create()
    # time.sleep(10)
    update()
    # delete()
