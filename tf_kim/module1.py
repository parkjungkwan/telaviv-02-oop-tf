# ***********************
# -- 
# ***********************
import tensorflow as tf
# CASE2
# 아래처럼 실행하면 40이 리턴됨
try :
    x = tf.constant([35, 40, 45], name='x')
    y = tf.Variable(x + 5, name='y')

    # 지금까지 정의한 변수를 Session 에서 사용할 수 있도록 초기화 합니다
    model = tf.global_variables_initializer()

    # with Session as 구분 사용시 Session 종료는 자동
    with tf.Session() as session:
        session.run(model)
        print(session.run(y))
except:
    print("ERROR-2")
