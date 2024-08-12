# 클래스의 상속 - 메서드 재정의(오버라이딩)

class Airplane:

    # __init__() 메서드 생략해도 기본적으로 작동한다.
    def __init__(self):
        print("비행기 클래스가 생성되었습니다.")

    def takeoff(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")

air1 = Airplane()
air1.takeoff()
air1.fly()
air1.land()

class Supersonicairplane(Airplane):
    # 비행 모드 : 1 - NORMAL / 2 - SUPERSONIC
    NORMAL = 1  # 클래스 상수(대문자 관례)
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = Supersonicairplane.NORMAL

    def fly(self):
        if self.fly_mode == Supersonicairplane.SUPERSONIC:
            print("비행기가 초음속으로 비행합니다.")
        else:
            super().fly()  #메서드 상속때도 super()
            # print("비행기가 일반 비행합니다.")

# 실행 영역
sa = Supersonicairplane()
sa.takeoff()
sa.fly()
sa.fly_mode = Supersonicairplane.SUPERSONIC
sa.fly()
sa.land()
