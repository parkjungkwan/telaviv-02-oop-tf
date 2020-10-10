import tensorflow as tf

# TensorFlow는 계산을 그래프로 표현해주는 프로그래밍 시스템이다.
a = tf.placeholder(tf.float32,[None,3])
# placeholder 는 매개변수
# 메타프로그래밍
# 심벌릭 변수
print(a)
# <결과>
# Tensor("Placeholder_4:0", shape=(?, 3), dtype=float32)
# <분석>
# shape 은 차원의 형태로 두번째 차원은 요소를 3개씩 가지고 있어야 함
w = tf.Variable(tf.random_normal([3,2]))
x = tf.Variable(tf.random_normal([2,1]))
# 정규분포의 무작위 값으로 초기화
# expr = tf.matmul(w,x) + b
b = tf.placeholder("float")
y = tf.multiply(a, b)
# 텐서객체 내부의 정의된 연산함수
sess = tf.Session()
print(sess.run(y, feed_dict = {a: 3, b: 3}))
# run() 메서드에 feed_dict 인수로 변수의 값을 입력함
# feed_dict 파라미터는 그래프를 실행할 때 사용할 입력값을 지정함
# To feed information into a computer means to gradually put it into it
