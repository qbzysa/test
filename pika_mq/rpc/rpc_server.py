# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/2/13 15:11
import pika


def get_channel():
    credentials = pika.PlainCredentials('qbz', '111111')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.16.230",
                                                                   port=5672,
                                                                   virtual_host="/",
                                                                   credentials=credentials,
                                                                   heartbeat_interval=300))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='rpc_queue')
    return channel


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    chl = get_channel
    print(" [x] Awaiting RPC requests")
    chl.start_consuming()
