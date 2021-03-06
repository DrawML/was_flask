"""
DrawML
Linear regression template file
Templates will be changed by appropriate value

There is some issues in input data
and maybe save model
"""
import tensorflow as tf
import numpy as np
import sys
import os

model_path = '/'
training_epoch = 1024

SAVE_PATH = '/Users/chan/test/trained_model'

def load_input():
    argc = len(sys.argv)
    if argc < 2:
        print('No input argument')
        sys.exit(2)

    file_path = sys.argv[1]
    if os.path.isfile(file_path) is False:
        print('No such file or directory', file_path)
        sys.exit(2)

    x = np.genfromtxt(file_path, max_rows=1)
    raw_data = np.genfromtxt(file_path, dtype='float32', skip_header=1)

    feature_size    = int(x[0])
    label_size      = int(x[1])

    x_data = raw_data[:, 0:feature_size]
    y_data = raw_data[:, feature_size:feature_size+label_size]

    return x_data, y_data, x_data, y_data, x_data, y_data


def make_optimizer():
    optimizer_module = tf.train
    optimizer_name   = 'GradientDescentOptimizer'
    optimizer_params = {'learning_rate': 0.01}
    return getattr(optimizer_module, optimizer_name)(**optimizer_params)


def save_model(sess, path):
    saver = tf.train.Saver()
    saver.save(sess, path)


def restore_model(sess, path):
    saver = tf.train.Saver()
    saver.restore(sess, path)


def load_train_data():
    data = {X: x_train, Y: y_train}
    return data


def make_model(X, W):
    reg_enable = True
    reg_lambda = 0.001
    model = tf.matmul(X, tf.transpose(W))
    if reg_enable is True:
        model += reg_lambda * tf.reduce_sum(tf.square(W))
    return model


def cost_function(hypothesis, Y):
    return tf.reduce_mean(tf.square(hypothesis - Y))


def init_weights():
    weight_init_module = tf.random_uniform
    weight_params      = {'maxval': 1.0, 'minval': -1.0}

    weight_params['shape'] = [1, len(x_train[0])]

    weight = tf.Variable(weight_init_module(**weight_params))
    return weight


x_train, y_train, x_valid, y_valid, x_test, y_test = load_input()

X = tf.placeholder(tf.float32)     # X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32)     # Y = tf.placeholder(tf.float32, [None, 10])

W = init_weights()
hypothesis = make_model(X, W)

cost = cost_function(hypothesis, Y)
optimizer = make_optimizer()
train = optimizer.minimize(cost)

with tf.Session() as sess:
    init = tf.initialize_all_variables()
    sess.run(init)
    train_data = load_train_data()
    for _ in range(training_epoch):
        sess.run(train, feed_dict=train_data)
        # some logging codes will be added...

    save_model(sess, SAVE_PATH)
    restore_model(sess, SAVE_PATH)

    print('features : original predict')
    p = sess.run(hypothesis, feed_dict=train_data)
    for i in range(len(x_test)):
        log = ''
        for j in range(len(x_test[i])):
            log += str(x_test[i][j]) + ' '
        log += ': '  + str(y_test[i]) + ' ' + str(p[i])
        print(log)
    print('Model Weights')
    print(sess.run(W))


