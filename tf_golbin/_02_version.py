# ***********************
# -- 3.1 버전 확인
# ***********************
version = tf.constant(tf.__version__)
sess = tf.Session()
print(sess.run(version))
