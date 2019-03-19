# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/7/16 9:15
import python_jwt as jwt


def unencrypt_RS256(key, token):
    print token
    header, claims = jwt.verify_jwt(token, key, ['RS256'])
    return header, claims


def unencrypt_PS256(key, token):
    print token
    header, claims = jwt.verify_jwt(token, key, ['PS256'])
    return header, claims


def unencrypt_ES256(key, token):
    print token
    header, claims = jwt.verify_jwt(token, key, ['ES256'])
    return header, claims


def unencrpyt_HS256(key, token):
    print token
    header, claims = jwt.verify_jwt(token, key, ['HS256'])
    return header, claims


