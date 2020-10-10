# ***********************
# -- 3.1 헬로우 텐서플로
# ***********************
import tensorflow as tf
# tf.placeholder(dtype,shape,name) 
a = tf.placeholder("float")
b = tf.placeholder("float")
""" placeholder는 초기값을 입력하지 않고 정의한다는 특징
    dtype : 플레이스홀더에 저장되는 데이타형이다. 
        tf.float32와 같이 실수,정수등의 데이타 타입을 정의한다.
    shape : 행렬의 차원을 정의한다. shapre=[3,3]으로 정의해주면, 
        이 플레이스홀더는 3x3 행렬을 저장하게 된다.
    name : name은 이 플레이스 홀더의 이름을 정의한다.
"""
# y = tf.mul(a,b) # 다음과 같은 에러 발생
# AttributeError: module 'tensorflow' has no attribute 'mul'
""" 스택오버
    tf.mul, tf.sub and tf.neg are deprecated in favor of tf.multiply, tf.subtract and tf.negative.
"""
y = tf.multiply(a,b)
sess = tf.Session()
print(sess.run(y, feed_dict={a : 3, b : 3}))
''' 파이썬 3 이상은 () 를 추가 '''

