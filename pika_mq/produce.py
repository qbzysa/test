# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/18 10:39
import pika
import json
from get_files import get_files_list
# 备注guest用户仅限于localhost连接，不能用于远程连接
# 会报exceptions.ProbableAuthenticationError错误
credentials = pika.PlainCredentials('qbz', '111111')


def send_message():
    # 创建一个连接
    # heartbeat_interval为心跳时间,超过心跳时间，与rabbitmq连接断开
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.16.230",
                                                                   port=5672,
                                                                   virtual_host="/",
                                                                   credentials=credentials,
                                                                   heartbeat_interval=300))
    # 创建通道
    channel = connection.channel()
    # 声明一个消息队列的名字为qbz,并设置该队列为持久化
    channel.queue_declare(queue='qbz', durable=True)

    file_list = get_files_list()
    for one_file in file_list:
        body = {"one_path": one_file}
        # 设置routing_key和body（发送的内容）
        # delivery_mode=2表示标记的任务为持久化存储
        channel.basic_publish(exchange='',
                              routing_key='qbz',
                              body=json.dumps(body),
                              properties=pika.BasicProperties(delivery_mode=2))   # delivery_mode=2设置发送的消息持久化
    # 关闭连接
    connection.close()


if __name__ == "__main__":
    send_message()
