#import tensorflow as tf
import torch
z = torch. arange(12, dtype=torch.float32)
print(z)
"""
x = tf.range(12, dtype=tf.float32)
tf.size(x)
x.shape
reshaping_x = tf.reshape(x, (3,4))

print(reshaping_x)

print(tf.zeros((2,3,4)))
print(tf.ones((3,3,4)))

tf.random.normal(shape=[2,2])

print(tf.exp(x))

x = tf.reshape(tf.range(12, dtype=tf.float32), (3,4))
y = tf.constant([[2.0, 1, 4, 3], [1,2,3,4], [4,3,2,1]])
print(tf.concat([x,y], axis=0), tf.concat([x,y],axis=1))

# Summing up all elemnts in tensor
print(tf.reduce_sum(x))
"""
"""
X_var = tf.Variable(x)
X_var[1,2].assign(9)
print(X_var)
"""

"""
import torch

x = torch.arange(12, dtype=torch.float32)

print(x)"""
