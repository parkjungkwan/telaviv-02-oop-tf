# ***********************
# -- 기초 연산
# ***********************
''' 파이썬은 변수의 타입이 고정되지 않은 
동적 타입(dynamically typed) 언어이다
'''
price = 1000
count = 5
total = price * count
total
# 자료형
'''
-- 접근방법
직접 direct : int, float, complex, bool
시퀀스 sequence : bytes, str, list, tuple
매핑 mapping : dict
-- 변경가능성
변경 가능 mutable : list, set, dict
변경 불가능 immutable : int, float, complex, bool, bytes, str, tuple
변수는 객체의 주소값을 가리킴
-- 저장모델
리터럴(literal) : int, float, complex, bool, bytes, str
저장(container) : list, tuple, dict, set
'''

# 예약어
import keyword
print(keyword.kwlist)
''' 
'False', 'None', 'True', 'and', 'as', 
'assert', 'break', 'class', 'continue', 'def', 
'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 
'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 
'while', 'with', 'yield'
'''
# 명령문
''' 연산문, 함수, 메소드, 일반 명령문" 등 4가지 형식의 명령문
연산문은 +(덧셈), -(뺄셈), *(곱셈), /(나눗셈) 또는 =(할당)과 같은 연산자
함수는 "함수(인수)" 형식
메소드는 "데이터.메소드( )" 형식
일반 명령문은 "조건문, 반복문, 선언문"
'''