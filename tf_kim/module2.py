# ***********************
# -- 
# ***********************
# numpy 를 사용해서 사이즈가 큰 데이터를 생성하고 식을 조금 복잡하게 수행
try:
    data = np.random.randint(1000, size=10000)
    x = tf.constant(data, name='x')
    y = tf.Variable(x**2 + 5*x + 5, name='y')
    model = tf.global_variables_initializer()
    with tf.Session() as session:
        session.run(model)
        print(session.run(y))
except:
    print("ERROR-3")
