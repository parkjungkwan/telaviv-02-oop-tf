from math import radians
import numpy as np     
import matplotlib.pyplot as plt
# matplotlib 설정하기
# 마이텐서플로 우클릭 > 파이썬 패키지 열기 > matplotlob 검색 > 설치

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()