# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/20 9:22
import pika


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


credentials = pika.PlainCredentials('qbz', '111111')
connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.16.230",
                                                               port=5672,
                                                               virtual_host="/",
                                                               credentials=credentials,
                                                               heartbeat_interval=300))
channel = connection.channel()
# 声明广播管道
channel.exchange_declare(exchange='fanout_test', type='fanout', durable=True)
# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
# 获取随机的queue名字
queue_name = result.method.queue
print("random queuename:", queue_name)
# 将queue绑定到exchange上
channel.queue_bind(exchange='fanout_test',  queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()

