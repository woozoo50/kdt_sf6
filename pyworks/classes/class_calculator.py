class Calculator:
    def __init__(self):
        self.x = 0  #멤버변수, 인스턴스 변수


    def add(self, y):
        self.x += y
        return self.x

    def sub(self, y):
        self.x -= y
        return self.x
'''
# 실행 영역
c1 = Calculator()
print(c1.x)
c2 = c1.add(10)  #c1.x에 10 더하기 , c2에 c1.x값 할당
print(c2)
c3 = c1.sub(5)   #c1.x에 5 빼기 , c3에 c1.x값 할당
print(c3)
c4 = c1.add(100) #c1.x에 100 더하기 , c4에 c1.x값 할당
print(c4)
c1.add(200)      #c1.x에 200 더하기
c5 = c1.add(111) #c1.x에 111 더하기 , c5에 c1.x값 할당
print(c5)

print(c1.sub(416))
print(c1.x)
'''