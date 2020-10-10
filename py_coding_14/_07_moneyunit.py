# ***********************
# -- 동전갯수
# ***********************
bill = int(input("금액을 입력하세요 : ")) #01
coin500 = bill // 500 #02
remainder = bill % 500 #03
coin100 = remainder // 100 #04
remainder = remainder % 100 #05
coin50 = remainder // 50 #06
remainder = remainder % 50 #07
coin10 = remainder // 10 #08
remainder = remainder % 10 #09
coin1 = remainder #10
print() #11
print("500원 개수 :", coin500)
print("100원 개수 :", coin100)
print("050원 개수 :", coin50)
print("010원 개수 :", coin10)
print("001원 개수 :", coin1) #12


