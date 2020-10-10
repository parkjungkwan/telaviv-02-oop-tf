# ***********************
# -- 메소드 선언
# ***********************
class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)  # 0 0
