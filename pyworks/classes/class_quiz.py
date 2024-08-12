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

if __name__ == "__main__": # 해당 구문이 사용된 파이썬 파일을 직접 실행했을 때만 아래 코드를 실행하겠다 (해당 파일 모듈로 사용할 시 main 실행되는 것 방지)
                           # 파이썬 파일을 커맨드라인이나 인터페이스를 통해 직접 실행한 경우 __name__에는 __main__이라는 값(네임스페이스)이 설정됨
                           # 다른 파일에서 불러와 사용하는 경우 __name__에는 __main__ 이 아닌 모듈 이름이 설정됨

    val = Calculator(8, 1)
    result_add = val.add()
    print(result_add)
    result_sub = val.sub()
    print(result_sub)
    result_mul = val.mul()
    print(result_mul)
    result_div = val.div()
    print(result_div)

'''
if __name__ == "classes.class_quiz":
    print("모듈 예시")
print(__name__)
'''

# 실습 2 - SuperMarket 클래스

class Supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        print(f"위치 : {self.location}")

    def change_category(self, category):
        self.product = category

    def show_list(self):
        print(f"상품 : {self.product}")

    def enter_customer(self):
        self.customer += 1

    def show_info(self):
        print(f"위치 : {self.location} / 이름 : {self.name} / 상품 : {self.product} / 고객 수 : {self.customer}")

if __name__ == "__main__":

    Mart = Supermarket("마포구 염리동", "마켓온", "가전", 0)
    for i in range(1,13):
        Mart.enter_customer()  #고객수 1씩 증가 12번 반복 0 -> 12

    Mart.change_category("음료")  #파는 물건 변경 : 가전 -> 음료

    Mart.print_location()  # 가게 위치 출력
    Mart.show_list()  # 현재 파는 물건 출력
    Mart.show_info()  # 가게 이름 / 위치 / 파는 물건 / 손님 수 모두 출력
