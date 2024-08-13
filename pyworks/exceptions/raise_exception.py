# raise exception - 예외 미루기
# 예외 처리를 미루면 호출하는 쪽에서 예외 처리를 함

class Aniaml:
    def breathe(self):
        print("숨을 쉰다.")

    def cry(self):  # 메서드를 구현하지 않고 미뤄둠 = 메서드를 구현하도록 강제함
        raise NotImplementedError
        # print("동물이 운다")

class Dog(Aniaml):
    def sleep(self):
        print("강아지가 잠을 잔다.")

    def cry(self):
        print("멍멍")


dog = Dog()
dog.breathe()
dog.sleep()
dog.cry()

class Cat(Aniaml):
    def sleep(self):
        print("고양이가 잠을 잔다.")

    def cry(self):
        print("야옹")
        
cat = Cat()
cat.breathe()
cat.sleep()
cat.cry()