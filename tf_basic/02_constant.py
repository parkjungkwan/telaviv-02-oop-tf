import tensorflow as tf
# ***********************
# -- 상수 생성 방법
# -- 날짜 : 2017/1/30
# -- 작성자 : https://3months.tistory.com/68
# ***********************
""" 기본 상수 """
t1 = [[1,2,3],[4,5,6]] # 2차원 배열
print(t1) # [[1, 2, 3], [4, 5, 6]]

t2 = tf.constant(t1) # 텐서플로우 상수 생성

print(t2) # Tensor("Const_9:0", shape=(2, 3), dtype=int32)
print(t2.get_shape()) # 2x3

t3 = tf.expand_dims(t2, 0) # 2-D 텐서를 3-D 텐서로 차원 확장

print(t3) # Tensor("ExpandDims_6:0", shape=(1, 2, 3), dtype=int32)
print(t3.get_shape()) # 1x2x3

# value 를 출력하려면 아래와 같이 세션 생성 후 run 해야함
sess = tf.Session()
print(sess.run(t2)) # [[1 2 3]
                         # [4 5 6]]
print(sess.run(t3)) #[[[1 2 3]
                                  # [4 5 6]]]

""" 상수를 생성하는 여러가지 방법 """
zeros_like = tf.zeros_like([4,3,3], dtype=tf.int32, name='zeros_like')
print(sess.run(zeros_like)) # [0,0,0] (입력으로 받은 텐서와 같은 shape의 텐서인데 0으로 초기화된 것)

# zeros와 zeros_like의 차이점 잘 비교. 일반적으로 zeros를 많이 쓸거 같음.
zeros = tf.zeros([3,4,5], dtype=tf.int32, name='zeros')
print(sess.run(zeros)) # 0으로 초기화된 3x4x5 텐서가 만들어짐

ones = tf.ones([2,2,3], dtype=tf.float32)
print(sess.run(ones)) # 1로 초기화된 2x2x3 텐서가 만들어짐

fill = tf.fill([2,3], 9) # 9로 초기화된 2x3 텐서
print(sess.run(fill))

contant = tf.constant([2,3,4]) # 주어진 텐서를 그대로 텐서플로우 변수로 전환
print(sess.run(contant)) # [2 3 4]

tensor = tf.constant(-1.0, shape=[2, 3])# tf.fill([2,3], -1.0) 과 같음
print(sess.run(tensor))
""" 난수 상수 생성 """
# 정규분포 난수
norm = tf.random_normal([2, 3], mean=-1, stddev=4)
print(sess.run(norm))

# 주어진 값들을 shuffle
c = tf.constant([[1, 2], [3, 4], [5, 6]])
shuff = tf.random_shuffle(c)
print(sess.run(shuff))
# [[5 6]
# [3 4]
# [1 2]]

# 균등분포 난수
unif = tf.random_uniform([2,3], minval=0, maxval=3)
print(sess.run(unif))
# [[2.6997993  0.74660575 1.4268554 ]
#  [1.8161677  0.17239559 0.91757405]]

""" 시퀀스 """
lin = tf.linspace(10.0, 12.0, 3, name="linspace")
print(sess.run(lin))

# start부터 시작하여 limit까지 (limit는 포함하지 않음) 
# delta의 증가량만큼 확장하며 정수 리스트를 생성합니다.

ran = tf.range(start=3, limit=7, delta=1) 
print(sess.run(ran)) # [3 4 5 6]

# start의 default는 0
ran2 = tf.range(8)
print(sess.run(ran2)) # [0 1 2 3 4 5 6 7]
""" 난수 생성시 seed의 활용 """
a = tf.random_uniform([1], seed=1) # seed를 주고 random한 값을 생성하면 매 session마다 값이 같음
b = tf.random_normal([1])

# Repeatedly running this block with the same graph will generate the same
# sequence of values for 'a', but different sequences of values for 'b'.
print("Session 1")
with tf.Session() as sess1:
  print(sess1.run(a))  # generates 'A1'
  print(sess1.run(a))  # generates 'A2'
  print(sess1.run(b))  # generates 'B1'
  print(sess1.run(b))  # generates 'B2'

print("Session 2")
with tf.Session() as sess2:
  print(sess2.run(a))  # generates 'A1'
  print(sess2.run(a))  # generates 'A2'
  print(sess2.run(b))  # generates 'B3'
  print(sess2.run(b))  # generates 'B4'
    
# tf.set_random_seed를 통해 모든 random value generation function들이 매번 같은 값을 반환함    
tf.set_random_seed(1234)
a = tf.random_uniform([1])
b = tf.random_normal([1])

# Repeatedly running this block with the same graph will generate different
# sequences of 'a' and 'b'.
print("Session 1")
with tf.Session() as sess1:
  print(sess1.run(a))  # generates 'A1'
  print(sess1.run(a))  # generates 'A2'
  print(sess1.run(b))  # generates 'B1'
  print(sess1.run(b))  # generates 'B2'

print("Session 2")
with tf.Session() as sess2:
  print(sess2.run(a))  # generates 'A1'
  print(sess2.run(a))  # generates 'A2'
  print(sess2.run(b))  # generates 'B1'
  print(sess2.run(b))  # generates 'B2'





