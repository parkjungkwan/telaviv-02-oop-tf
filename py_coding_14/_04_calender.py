# ***********************
# -- 달력
# ***********************
import calendar
year = int(input("년도"))
month = int(input("월"))
print()
cal = calendar.month(year,month)
print(cal)
cal = calendar.calendar(year, w = 2, l = 1, c = 6) 
# w : 날짜간격, l : 주의 상하라인, c : 월간의 간격
print(cal)


