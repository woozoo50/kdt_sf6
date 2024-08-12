# 정보 은닉(Informaition Hiding)
class Health:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def getname(self):
        return self.__name

    def sethp(self, hp):
        if hp < 0:
            hp = 0
        elif hp > 100:
            hp = 100
        self.__hp = hp

    def gethp(self):
        return "hp : " + str(self.__hp)

    def exercise(self, hours):
        self.sethp(self.__hp + hours)
        print("{}시간 운동하다".format(hours))

    def drink(self, cups):
        self.sethp(self.__hp - cups)
        print("술을 {}잔 마시다".format(cups))

p1 = Health("나몸짱")
p1.sethp(150)  # hp 100 이상 올라가지 않음
print(f'{p1.getname()} ※ {p1.gethp()}')
p1.drink(10)  # hp 10 감소
print(f'{p1.getname()} ※ {p1.gethp()}')
p1.exercise(5)  # hp 5 증가
print(f'{p1.getname()} ※ {p1.gethp()}')

print("--------------------------------------")

p2 = Health("player2")
print(f'{p2.getname()} ※ {p2.gethp()}')
p2.exercise(10)  # hp 초기값 100 , 100 이상 올라가지 않음
print(f'{p2.getname()} ※ {p2.gethp()}')
p2.drink(1000)  # hp 0 이하로 떨어지지 않음
print(f'{p2.getname()} ※ {p2.gethp()}')

