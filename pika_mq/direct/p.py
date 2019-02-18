# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/2/12 17:10
import pika

credentials = pika.PlainCredentials('qbz', '111111')

connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.16.230",
                                                               port=5672,
                                                               virtual_host="/",
                                                               credentials=credentials,
                                                               heartbeat_interval=300))

channel = connection.channel()
channel.exchange_declare(exchange='logs_direct_test1', type='direct')

serverity = 'error'
msg = 'test'
for i in range(10):
    channel.basic_publish(exchange='logs_direct_test1',
                          routing_key=serverity,
                          body=msg+str(i),
                          properties=pika.BasicProperties(delivery_mode=2))

print('开始发送:%r:%r'% (serverity, msg))
connection.close()