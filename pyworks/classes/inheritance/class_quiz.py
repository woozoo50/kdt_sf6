# 실습 3
# 모듈(Module) 불러오기
from classes.class_calculator import Calculator
import sys

class LimitCalculator(Calculator):
    def __init__(self):
        self.x= 100

    def sub(self, y):
        self.x -= y
        if self.x >= 0:
            self.x = self.x
        elif self.x < 0:
            self.x = 0
        return self.x
    '''
    super().sub(y)
    if self.x < 0:
        self. x = 0
    :return self.x
    '''

# 실행 코드
c = Calculator()
lc = LimitCalculator()

print(c.sub(20))
print(c.sub(90))

print(lc.sub(20))
print(lc.sub(90))



'''
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
