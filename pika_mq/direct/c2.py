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
channel.basic_qos(prefetch_count=1)
channel.exchange_declare(exchange='logs_direct_test1', type='direct')
#随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

serverities = ['error', ]
for serverity in serverities:
    channel.queue_bind(exchange='logs_direct_test1', queue=queue_name, routing_key=serverity)
print('[***] 开始接受消息!')


def callback(ch, method, properties, body):
    print('[x] %r:%r' % (method.routing_key, body))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue=queue_name, no_ack=False)
channel.start_consuming()