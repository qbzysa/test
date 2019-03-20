from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# 加载MNIST数据
mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)

# 创建x, x是一个占位符，代表待识别的图片
x = tf.placeholder(tf.float32, [None, 784])
# W是Softmax模型的参数，将一个784维的输入转换成一个10维的输出
W = tf.Variable(tf.zeros([784, 10]))
# b也是Softmax模型的参数，一般叫作“偏置项”
b = tf.Variable(tf.zeros([10]))
# y表示模型的输出，一般叫作"预测值"
y = tf.matmul(x, W)+b
# 输入的真实值的占位
y_ = tf.placeholder(tf.float32, [None, 10])
# 我们用tf.nn.softmax_cross_entropy_with_logits 来计算预测值y与真实值y_的差值，并取均值
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_, logits=y))
# 采用SGD作为优化器，用梯度下降法针对模的参数(W和b)进行优化，0.5表示梯度下降优化器使用的学习率
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 创建一个Session，只有在session中才能运行优化步骤train_step
sess = tf.InteractiveSession()
# 初始化所有变量，并分配内存
tf.global_variables_initializer().run()
# 进行1000梯度下降
for _ in range(1000):
    # 在mnist.train中取100个训练数据
    # batch_xs是形状为(100, 784)的图像数据
    # batch_ys是形如(100, 10)的实际标签
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 正确的预测结果
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# 计算预测准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 计算模型在测试集上的准确率
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

