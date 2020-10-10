# ***********************
# -- 성적표
# ***********************
name=input("이름을 입력하세요 : ") #01
kor=int(input("국어 점수 : ")) #02
eng=int(input("영어 점수 : ")) #03
mat=int(input("수학 점수 : ")) #04
tot=kor+eng+mat #05 총점계산
ave=tot/3 #06 평균계산
ave=round(ave, 2) #07 평균을 소수이하 2자리로 조절
print() #08
print("총점 : ", tot) #09
print("평균 : ", ave) #10
