import random
def act():
    rps_dict = {"가위" : 1, "바위" : 2, "보" : 3}
    print(" 그만 하려면 Ctrl + c 를 눌르면 됩니다!")

while(True):
    rps_dict = {"가위" : 1, "바위" : 2, "보" : 3}
    print(" 그만 하려면 Ctrl + c 를 눌르면 됩니다!")

    while(True):
        print("_____나 : ", end="")
        myIn = rps_dict[input()]
        if myIn == 1 or myIn ==2 or myIn ==3:
            computerIn__ = random.choice(["가위", "바위", "보"])
            print("컴퓨터 : {}".format(computerIn__))
			
            computerIn = rps_dict[computerIn__]
			
            if myIn == computerIn:
                print(" 비겼음")
            elif (myIn == 1 and computerIn == 2) or (myIn == 2 and computerIn == 3) or (myIn == 3 and computerIn == 1):
                print(" 졌음......")
            else:
                print(" 이겼음!!!!")
            print("")
        else:
            print("가위, 바위, 보 중에 하나를 내세요!")

if __name__ == "__main__":
    act()