# ***********************
# -- 가위바위보
# ***********************
import random #01
print("1, 2, 3 중 하나를 선택하세요.") #02
user = int(input("가위-1, 바위-2, 보-3 : ")) #03
computer = random.randint(1, 3) #04
if user == computer: #05
    print("비겼어요!") #06
elif user == 1: #07
    if computer == 2: #08
        print() #09
        print("컴퓨터가 이겼어요!") #10
        print("당신은 '가위'입니다.")
        print("컴퓨터는 '바위'입니다.") #11
    else: #12
        print() #13
        print("당신이 이겼어요!")
        print("당신은 '가위'입니다.")
        print("컴퓨터는 '보'입니다.") #14
elif user == 2:
    if computer == 1:
        print()
        print("당신이 이겼어요!")
        print("당신은 '바위'입니다.")
        print("컴퓨터는 '가위'입니다.")
    else:
        print()
        print("컴퓨터가 이겼어요!")
        print("당신은 '바위'입니다.")
        print("컴퓨터는 '보'입니다.")
elif user == 3:
    if computer == 1:
          print()
          print("컴퓨터가 이겼어요!")
          print("당신은 '보'입니다.")
          print("컴퓨터는 '가위'입니다.")
    else:
          print()
          print("당신이 이겼어요!")
          print("당신은 '보'입니다.")


