import tensorflow as tf
# ***********************
# -- 변수 생성 방법
# -- 날짜 : 2017/1/30
# -- 작성자 : reference : https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/g3doc/how_tos/variables/
# ***********************
# 두 변수를 생성.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
biases = tf.Variable(tf.zeros([200]), name="biases")

# 변수는 반드시 initialization 해야한다.
# 변수 초기화

# 두 변수를 생성
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
biases = tf.Variable(tf.zeros([200]), name="biases")

# 변수 초기화 오퍼레이션을 초기화
init_op = tf.global_variables_initializer()

# 나중에 모델을 실행할때
with tf.Session() as sess:
    sess.run(init_op) # initialization 연산 실행
    print(sess.run(weights))
    print(sess.run(biases))
    # 다른 변수값을 참조하여 초기화 하기

# 랜덤 값으로 새로운 변수 초기화
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
# weights와 같은 값으로 다른 변수 초기화
w2 = tf.Variable(weights.initialized_value(), name="w2")
# weights의 2배 값으로 다른 변수 초기화
w_twice = tf.Variable(weights.initialized_value() * 2.0, name="w_twice")

# 변수 초기화 오퍼레이션을 초기화
init_op = tf.global_variables_initializer()

with tf.Session() as sess : 
    sess.run(init_op)
    print(sess.run(w2))
    print(sess.run(w_twice))




