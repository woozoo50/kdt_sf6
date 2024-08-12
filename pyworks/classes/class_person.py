# 정보 은닉(보안을 유지하기 위해 접근을 허용하지 않는 것)
# 접근 제어자 - public(기본), private, protected

class Person:
    # 언더 스코어 2개 (__) 를 넣으면 접근할 수 없음

    def __init__(self):
        # self.name = ("")
        self._name = ""  # private
        self._age = 0

    # 접근하기 위해서 get , set 매서드를 만들어서 접근

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age
    
# 실행 영역
p1 = Person()
# p1.name = "Jerry"
# p1 = Person("Jerry:)
# print(p1.name)

p1.set_name("Jerry")
print(p1.get_name())

# print(p1._name)

p1.set_age(20)
print(p1.get_age())

