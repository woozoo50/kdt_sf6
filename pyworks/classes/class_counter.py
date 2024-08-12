# 카운터 만들기 - 클래스 변수

class Counter:
    x = 0
    def __init__(self):
        Counter.x += 1

c1 = Counter()
print(c1.x)

c2 = Counter()
print(c1.x)

c3 = Counter()
print(c3.x)

c4 = Counter()
print(Counter.x)

class Counter2:
    def __init__(self):
        self.x = 0  #인스턴스 변수
        self.x += 1

count1 = Counter2()
print(count1.x)

count2 = Counter2()
print(count2.x)