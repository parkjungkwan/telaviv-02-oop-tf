# ***********************
# -- 스태틱방식의 메소드 호출
# -- invoking method statically
# ***********************
class Point:
    def reset(self):
        self.x = 0
        self.y = 0
p = Point()
Point.reset(p)
print(p.x, p.y) # 0 0
