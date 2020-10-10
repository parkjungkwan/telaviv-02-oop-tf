# ***********************
# -- 성적표
# ***********************
class Grade:
    def calc(score):
        if score >= 90: #02
            grade = "A" #03
            msg = "장학금 100만원이 지급됩니다." #04
        elif score >= 80: #05
            grade = "B" #06
            msg = "장학금 50만원이 지급됩니다." #07
        elif score >= 70: #08
            grade = "C" #09
            msg = "장학금 대상이 아닙니다." #10
        elif score >= 60: #11
            grade = "D" #12
            msg = "장학금 대상이 아닙니다." #13
        else: #14
            grade = "F" #15
            msg = "낙제입니다. 재수강하세요." #16
            print() #17
            print(grade + " 학점입니다.") #18
g = Grade() 
score = int(input("점수를 입력하세요 : ")) #01
res = g.calc(score)
print(msg) #19
