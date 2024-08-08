# 생성자(constructor) der __int__()
# self를 이용해서 표현

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def show_info(self):
        print(f'모델명 : {self.model}, 연식 : {self.year}')

# car_a는 메모리 힙(hear)을 사용한다.
car_a = Car("아이오닉6", 2023)
car_a.show_info()

car_b = Car("스포티지", 2020)
car_b.show_info()

# 객체 리스트 만들기
cars = [
    Car("소나타", 2020),
    Car("K5", 2017),
    Car("모닝", 2022)
]

cars[0].show_info()
cars[-1].show_info()

print("***** 승용차 List *****")
for i in cars:
    i.show_info()
