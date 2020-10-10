# ***********************
# -- MNIST 단일 계층 신경망 트레이닝
# -- 날짜 : 2017/2/1
# -- 환경 : windows tensorflow, anaconda 4.3, python 3.5
# -- 작성자 : https://3months.tistory.com/68
# ***********************
""" Tensorflow를 통해 단일 계층 신경망을 구축하고 MNIST 데이터를 training하고 test 하는 예제입니다. 
    많은 예제들이 tensorflow 내부에 example로 있는 MNIST 데이터를 이용하지만 
    이 포스팅에서는 외부에 있는 MNIST pickle 파일을 다운로드하고 이를 읽어들여 모델을 구축해보았습니다. 
    사용한 MNIST pickle 파일은 https:na//github.com/mnielsen/neural-networks-and-deep-learning/blob/master/data/mnist.pkl.gz 이곳에서 다운로드 받을 수 있습니다.
    출처: https://3months.tistory.com/73?category=755918 [Deep Play] 
"""
# 1. 데이터 읽기
import tensorflow as tf
import gzip, numpy
import pickle as cPickle
import pandas as pd
# No module named 'pandas'
# Load the dataset
f = open('data/mnist.pkl', 'rb')
train_set, valid_set, test_set = cPickle.load(f, encoding='latin1')
f.close()

x_train, y_train = train_set
x_test, y_test = test_set
""" pickle로 불러온 변수에는 train_set, valid_set, test_set이 나뉘어져 있기 때문에 
    위와 같이 load하면 알아서 training, validation, test set으로 나눌 수 있습니다. 
    또한 각각은 튜플 자료구조형으로 또 다시 x, y로 나뉘어져 있기 때문에 
    x_train, y_train = train_set 구문을 통해 feature과 label을 분리할 수 있습니다. 
    이렇게 데이터를 빠르게 training을 적용할 수 있는 형태로 만들어낼 수 있다는 것이 
    pickle 파일의 좋은 점입니다. 
    하지만 예제가 아닌 실제 머신러닝 모델을 구축할 때는 이러한 과정을 모두 직접하여야 합니다. 
    이미지 파일을 읽어들여야하고 또 이것을 적절한 사이즈의 numpy array로 바꾸어야합니다. 
"""
# 2. 데이터 전처리
y_train = pd.get_dummies(y_train)
y_test = pd.get_dummies(y_test)
# label들을 one hot encoding합니다. 
# tensorflow에서는 label을 one hot encoding 하여 제공하여야 합니다.
print('x_train shape : ',x_train.shape) # (50000, 784)
print('y_train shape : ',y_train.shape) # (50000, 10)
print('x_test shape : ',x_test.shape) # (10000, 784)
print('y_test shape : ',y_test.shape) # (10000, 10)

