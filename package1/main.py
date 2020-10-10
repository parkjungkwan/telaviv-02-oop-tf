import package1.class1    # calcpkg 패키지의 operation 모듈을 가져옴
import package1.class2     # calcpkg 패키지의 geometry 모듈을 가져옴
if __name__ == "__main__":
    c1 = package1.Operation()
    c2 = package1.Geometry()
    print(c1.add(10, 20))    # operation 모듈의 add 함수 사용
    print(c2.mul(10, 20))    # operation 모듈의 mul 함수 사용
 
    print(c2.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
    print(c2.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용
