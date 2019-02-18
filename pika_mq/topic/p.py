# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/2/12 17:17
import pika
import sys

credentials = pika.PlainCredentials('qbz', '111111')

connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.16.230",
                                                               port=5672,
                                                               virtual_host="/",
                                                               credentials=credentials,
                                                               heartbeat_interval=300))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()