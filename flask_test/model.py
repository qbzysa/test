# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/24 13:48
from api import db
from sqlalchemy import Column, String


# 定义User对象:
class User(db.Model):
    # 表的名字:
    __tablename__ = 'test'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(255))
    age = Column(String(255))



