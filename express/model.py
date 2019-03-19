# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/24 13:48
from kd_api import db
from sqlalchemy import Column, String


# 定义User对象:
class KD(db.Model):
    # 表的名字:
    __tablename__ = 'kuaidi'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    url = Column(String(255))
    name = Column(String(255))
    type = Column(String(255))
    image = Column(String(255))



