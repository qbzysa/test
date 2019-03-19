# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/1/22 13:18
from wxpy import *
bot = Bot(cache_path=True)
tmp = bot.friends().search(u'我的未来不是你！')[0]


# @bot.register()
# def print_others(msg):
#     print(msg)


# 回复my_friend发送的消息
@bot.register(tmp)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)


# # 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
# @bot.register(bot.self, except_self=False)
# def reply_self(msg):
#     print msg
#     return msg
#
#
# # 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# # 这条注册消息是我们构建群聊机器人的基础
# @bot.register(Group, TEXT)
# def print_group_msg(msg):
#     if msg.is_at:
#         print(msg)
#         msg.reply(msg.text)

embed()
