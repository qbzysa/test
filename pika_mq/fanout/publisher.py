# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/20 9:22
import pika
import sys
credentials = pika.PlainCredentials('qbz', '111111')

connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.16.230",
                                                               port=5672,
                                                               virtual_host="/",
                                                               credentials=credentials,
                                                               heartbeat_interval=300))
channel = connection.channel()
# 注意：这里是广播，不需要声明queue
channel.exchange_declare(exchange='fanout_test',  # 声明广播管道
                         type='fanout',
                         durable=True)

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!"
channel.basic_publish(exchange='fanout_test',
                      routing_key='',  # 注意此处空，必须有
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))  # delivery_mode=2设置发送的消息持久化
print(" [x] Sent %r" % message)
connection.close()