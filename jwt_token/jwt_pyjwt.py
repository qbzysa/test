# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/11/22 17:38
import jwt
import jwcrypto.jwk as jwk
import time
from datetime import datetime
from calendar import timegm
from os import urandom
from jwcrypto.common import base64url_encode

RS_key = jwk.JWK.generate(kty='RSA', size=2048)
PS_key = jwk.JWK.generate(kty='RSA', size=2048)
HS_key = jwk.JWK.generate(kty='oct', size=2048)
ES_key = jwk.JWK.generate(kty='EC', size=2048)

playload = {
        "username": "qbz",
        "aud": "qbz",
        "org_code": "000000000000",
        "iss": "test",
        "uuid": "9321D3769B755CC5A304C5446E843088",
        "exp": int(time.time())+86400*7,
        "iat": int(time.time()),
        "sub": "9321D3769B755CC5A304C5446E843088"
    }


def encrypt_HS256(playload):
    now = datetime.utcnow()
    playload['nbf'] = timegm(now.utctimetuple())
    playload['jti'] = base64url_encode(urandom(16))
    token = jwt.encode({'claims': playload}, str(HS_key), algorithm='HS256')
    return token


def unencrypt_HS256(token):
    claims = jwt.decode(token, str(HS_key), algorithms=['HS256'])
    return claims


def encrypt_PS256(playload):
    now = datetime.utcnow()
    playload['nbf'] = timegm(now.utctimetuple())
    playload['jti'] = base64url_encode(urandom(16))
    priv_pem = PS_key.export_to_pem(private_key=True, password=None)
    token = jwt.encode({'claims': playload}, priv_pem, algorithm='PS256')
    return token


def unencrypt_PS256(token):
    pub_pem = PS_key.export_to_pem()
    claims = jwt.decode(token, pub_pem, algorithms=['PS256'])
    return claims


def encrypt_ES256(playload):
    now = datetime.utcnow()
    playload['nbf'] = timegm(now.utctimetuple())
    playload['jti'] = base64url_encode(urandom(16))
    priv_pem = ES_key.export_to_pem(private_key=True, password=None)
    token = jwt.encode({'claims': playload}, priv_pem, algorithm='ES256')
    return token


def unencrypt_ES256(token):
    pub_pem = ES_key.export_to_pem()
    claims = jwt.decode(token, pub_pem, algorithms=['ES256'])
    return claims


def encrypt_RS256(playload):
    now = datetime.utcnow()
    playload['nbf'] = timegm(now.utctimetuple())
    playload['jti'] = base64url_encode(urandom(16))
    priv_pem = RS_key.export_to_pem(private_key=True, password=None)
    token = jwt.encode({'claims': playload}, priv_pem, algorithm='RS256')
    return token


def unencrypt_RS256(token):
    pub_pem = RS_key.export_to_pem()
    claims = jwt.decode(token, pub_pem, algorithms=['RS256'])
    return claims


if __name__ == "__main__":
    data1 = encrypt_HS256(playload)
    print unencrypt_HS256(data1)
    data2 = encrypt_PS256(playload)
    print unencrypt_PS256(data2)
    data3 = encrypt_ES256(playload)
    print unencrypt_ES256(data3)
    data4 = encrypt_RS256(playload)
    print unencrypt_RS256(data4)
    print data1
    print data2
    print data3
    print data4