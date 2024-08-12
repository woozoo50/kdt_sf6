# 모듈(Module) 불러오기
from classes.class_quiz import Calculator
import sys

# 객체 생성
calc = Calculator(4, 5)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())

class MoreCalculator(Calculator):
    # 거듭 제곱 계산 기능 추가

    def pow(self):
        return self.num1 ** self.num2

    def devide(self):
        try:
            super().div()
        except:
            print("0으로 나눌 수 없습니다.")
            sys.exit(0)

mc = MoreCalculator(6, 0)
print(mc.pow())
print(mc.div())

"""
# 참고
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        if self.num2 == 0:
            print("0으로 나눌 수 없음")
            #return self.num1
            return sys.exit(0)
        else:
            return self.num1 / self.num2

val = Calculator(8, 0)
result_add = val.add()
print(result_add)
result_sub = val.sub()
print(result_sub)
result_mul = val.mul()
print(result_mul)
result_div = val.div()
print(result_div)

"""