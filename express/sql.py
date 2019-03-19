# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/24 13:43
from model import KD

def get_all():
    return KD.query.all()