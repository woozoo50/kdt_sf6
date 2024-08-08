# 실습 1 - 사칙연산 클래스 만들기
import sys

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
