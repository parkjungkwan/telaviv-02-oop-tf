# ***********************
# -- 텐서플로우 심볼릭 변수 (플레이스홀더) 생성 방법
# -- 날짜 : 2017/1/30
# -- 작성자 : reference : https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/g3doc/how_tos/variables/
# ***********************
import tensorflow as tf
""" 실행시에 데이터를 제공하는 방법으로 실제 딥러닝 모델 구축시 많이 쓰인다.  
    sess.run 에서 feed_dict에 dictionary 형식으로 값을 넣어주면 되고 
    이를 feeding이라 한다.
"""
a = tf.placeholder("float")
b = tf.placeholder("float")
y = tf.multiply(a,b)
sess = tf.Session()

print(sess.run(y, feed_dict={a : 3, b: 5})) # 15.0


