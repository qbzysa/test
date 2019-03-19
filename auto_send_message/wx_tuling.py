# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/23 15:01
import json
import requests
from wxpy import *

bot = Bot(console_qr=True, cache_path=True)
tmp = bot.friends().search(u'我的未来不是你！')[0]


# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "003b1af8edc14394a6558dd1afc77cad"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"}
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[tuling] " + result["text"]


@bot.register(tmp)
def forward_message(msg):
    return auto_reply(msg.text)
embed()