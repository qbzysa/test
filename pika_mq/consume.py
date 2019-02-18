# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/18 10:47
import pika
import time
import json
from un_file import un_zip
credentials = pika.PlainCredentials('qbz', '111111')


# 创建一个连接
# heartbeat_interval为心跳时间,没有及时发送心跳，将会与rabbitmq连接断开
def get_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.16.230",
                                                                   port=5672,
                                                                   virtual_host="/",
                                                                   credentials=credentials,
                                                                   heartbeat_interval=300))
    channel = connection.channel()
    # 如果生产者没有运行创建队列，那么消费者也许就找不到队列了。
    # 为了避免这个问题，所有消费者也创建这个队列，如果队列已经存在，则这条无效。
    channel.queue_declare(queue='qbz', durable=True)
    # 设置rabbitmq不给正在处理的消费者，下发消息
    channel.basic_qos(prefetch_count=1)
    # 调callback函数
    # no_ack = true为自动应答,即接受到消息，立即回复ack
    # no_ack = false为手动应答
    channel.basic_consume(callback, queue='qbz', no_ack=False)
    # 创建死循环，监听消息队列，可使用CTRL+C结束监听
    print ' [*] Waiting for messages. To exit press CTRL+C'
    channel.start_consuming()


# 回调函数，获取消息体
def callback(ch, method, properties, body):
    zip_file = str(json.loads(body).get('one_path'))
    print "Received %r" % zip_file
    un_zip(str(zip_file))
    # 消费者接受任务，并处理完成后，给rabbitmq返回确认
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    start = time.time()
    get_message()
    end = time.time()
    print end - start