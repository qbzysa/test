# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/7/17 9:49

import python_jwt as jwt, jwcrypto.jwk as jwk
import time
from jwt_unencrypt import unencrpyt_HS256, unencrypt_RS256, unencrypt_ES256, unencrypt_PS256

RS_key = jwk.JWK.generate(kty='RSA', size=2048)
PS_key = jwk.JWK.generate(kty='RSA', size=2048)
HS_key = jwk.JWK.generate(kty='oct', size=2048)
ES_key = jwk.JWK.generate(kty='EC', size=2048)


def encrypt_RS256():
    priv_pem = RS_key.export_to_pem(private_key=True, password=None)
    pub_pem = RS_key.export_to_pem()
    payload = {
             "iss": "Online JWT Builder",
             "iat": int(time.time()),
             "exp": int(time.time()) + 86400 * 7,
             "aud": "www.gusibi.com",
             "sub": "uid",
             "nickname": "goodspeed",
             "username": "goodspeed",
             "scopes": ["admin", "user"]
         }
    priv_key = jwk.JWK.from_pem(priv_pem)    # 生成私钥
    pub_key = jwk.JWK.from_pem(pub_pem)      # 生成公钥
    rs_token = jwt.generate_jwt(payload, priv_key, 'RS256')
    #认证
    header, claims = unencrypt_RS256(pub_key, rs_token)
    print header
    print claims


def encrypt_PS256():
    payload = {
             "iss": "Online JWT Builder",
             "iat": int(time.time()),
             "exp": int(time.time()) + 86400 * 7,
             "aud": "www.gusibi.com",
             "sub": "uid",
             "nickname": "goodspeed",
             "username": "goodspeed",
             "scopes": ["admin", "user"]
         }
    ps_token = jwt.generate_jwt(payload, PS_key, 'PS256')
    #认证
    header, claims = unencrypt_PS256(PS_key, ps_token)
    print header
    print claims


def encrypt_HS256():
    payload = {
        "iss": "Online JWT Builder",
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        "aud": "www.gusibi.com",
        "sub": "uid",
        "nickname": "goodspeed",
        "username": "goodspeed",
        "scopes": ["admin", "user"]
    }
    hs_token = jwt.generate_jwt(payload, HS_key, 'HS256')
    #认证
    header, claims = unencrpyt_HS256(HS_key, hs_token)
    print header
    print claims


def encrypt_ES256():
    payload = {
        "iss": "Online JWT Builder",
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        "aud": "www.gusibi.com",
        "sub": "uid",
        "nickname": "goodspeed",
        "username": "goodspeed",
        "scopes": ["admin", "user"]
    }
    es_token = jwt.generate_jwt(payload, ES_key, 'ES256')
    #认证
    header, claims = unencrypt_ES256(ES_key, es_token)
    print header
    print claims


if __name__ == "__main__":
    encrypt_RS256()
    encrypt_PS256()
    encrypt_HS256()
    encrypt_ES256()