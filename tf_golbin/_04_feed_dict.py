# ***********************
# -- 3.2 플레이스홀더와 변수
# ***********************
import tensorflow as tf
X = tf.placeholder(tf.float32,[None,3])
print(X)
# <결과> Tensor("Placeholder_7:0", shape=(?, 3), dtype=float32)
x_data = [[1,2,3],[4,5,6]]
W = tf.Variable(tf.random_normal([3,2]))
b = tf.Variable(tf.random_normal([2,1]))
expr = tf.matmul(X,W) + b
sess = tf.Session()
# sess.run(tf.global_variables_intializer()) 에러발생
"""
<스택오버>
I got the same error. However this is my solution: just skip the init = tf.global_variables_initializer()
  and just use : sess = tf.Session sess.run(init = tf.global_variables_initializer())
"""
init = tf.global_variables_initializer()
print("=== x_data ===")
print(x_data)  # [[1, 2, 3], [4, 5, 6]]
print("=== W ===")
print(sess.run(W)) # exception occurred
print("=== b ===")
print(sess.run(b))
print("=== expr ===")
print(sess.run(expr, feed_dict = {X: x_data}))

sess.close()