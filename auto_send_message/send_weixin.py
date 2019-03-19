# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/21 10:46
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import random
bot = Bot(cache_path=True)


def get_news():
    """获取金山词霸每日一句，英文和翻译"""

    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news():
    try:
        content, note = get_news()
        # 你朋友的微信名称，不是备注，也不是微信帐号。
        # my_friend = bot.groups().search(u'吃饭群')[0]
        my_friend = bot.friends().search(u'韬声依旧')[0]
        # my_friend.send_file(u'E:\\test\\auto_send_message\\test.txt')
        my_friend.send(content)
        my_friend.send(note)
        my_friend = bot.friends().search(u'江左')[0]
        # my_friend.send_file(u'E:\\test\\auto_send_message\\test.txt')
        my_friend.send(content)
        my_friend.send(note)
        # 每86400秒（1天），发送1次
        # 为了防止时间太固定，于是决定对其加上随机数
        ran_int = random.randint(0, 100)
        t = Timer(86400 + ran_int, send_news)
        t.start()
    except Exception as e:
        print e
        bot.file_helper.send(u'发送消息失败!')


if __name__ == "__main__":
    send_news()
    embed()


