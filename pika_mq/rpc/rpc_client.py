# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/2/13 15:11
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.credentials = pika.PlainCredentials('qbz', '111111')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.16.230",
                                                                            port=5672,
                                                                            virtual_host="/",
                                                                            credentials=self.credentials,
                                                                            heartbeat_interval=300))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                   correlation_id=self.corr_id),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


if __name__ == "__main__":
    fibonacci_rpc = FibonacciRpcClient()
    for i in range(30):
        print(" [x] Requesting fib(%s)" % i)
        response = fibonacci_rpc.call(i)
        print(" [.] Got %r" % response)
