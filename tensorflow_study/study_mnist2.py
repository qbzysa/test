# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/3/7 8:58
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# 加载MNIST数据
mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W)+b  # 预测值
# 输入的真实值的占位
y_ = tf.placeholder(tf.float32, [None, 10])
# 我们用tf.nn.softmax_cross_entropy_with_logits 来计算预测值y与真实值y_的差值，并取均值
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_, logits=y))
# 采用SGD作为优化器
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 计算预测值和真实值
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# 布尔型转化为浮点数，
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# 并取平均值，得到准确率
# 计算模型在测试集上的准确率
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
