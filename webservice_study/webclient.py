# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/23 9:59
from suds.client import Client

client = Client("http://192.168.16.166:8088?wsdl")
req1 = client.service.make_project1("QBZ", "1.0.0")

names = client.factory.create("stringArray")
name = "ysa"
names.string.append(name)
names.string.append(name)
req2 = client.service.make_project2(names)

name = {}

name["first_name"] = "Benzhao"
name["last_name"] = "Qiu"
names = client.factory.create("SnameArray")
names.Sname.append(name)
req3 = client.service.make_project(names)

