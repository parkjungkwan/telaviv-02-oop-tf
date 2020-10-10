# ***********************
# -- 세금
# ***********************
price = int(input("정 가 : ")) #01
rate = float(input("할인율 : "))/100 #02
discount = price * rate #03
pay = price - discount #04
tax = pay * 0.1 #05
pay = pay + tax #06
print() #07
print("할인액 :", int(discount)) #08
print("세 금 :", int(tax)) #09
print("지불액 :", int(pay)) #10
