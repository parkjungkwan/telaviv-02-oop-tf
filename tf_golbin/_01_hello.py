# ***********************
# -- 3.1 헬로우 텐서플로
# ***********************
import tensorflow as tf

hello = tf.constant("Hello, Tensorflow !!")
print(hello) # Tensor("Const_2:0", shape=(), dtype=string)
""" constant 는 상수 텐서를 생성하는 함수
    텐서라는 자료형에 상수를 담고 있다 
""" 
sess = tf.Session()
""" 심벌릭 표현으로 된 수식을 계산하기 위해 세션 생성
    머신러닝 표현 : 인터페이스
    머신러닝 실행 : 프로그램
    머신러닝은 인공지능의 부분집합
    머신러닝은 패턴을 통해 예측
    딥러닝은 머신러닝의 부분집합
    딥러닝은 심층신경망(DNN) 구현
    텐서플로우에서는 수식의 정의만으로 연산이 수행되지 않으며, 
    텐서(Tensor)에 데이터를 넣어주어야 비로소 연산을 수행하게 됩니다.
    이렇게 데이터를 넣어주는 동작을 세션(Session)이라고 합니다. 
"""
print(sess.run(hello))  # b'Hello, Tensorflow !!'
""" 파이썬 3 이상에서는 print() 괄호사용 """

