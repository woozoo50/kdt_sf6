# 단위 변환기 클래스 만들기

class ScaleConverter:
    # 생성자 메서드
    def __init__(self, units_from, unit_to, factor):
        self.units_from = units_from  # 단위
        self.units_to = unit_to  # 변환할 단위
        self.factor = factor  # 변환값

    # 단위 변환 메서드
    def convert(self, value):
        return self.factor * value

    def __str__(self):
        return f'{self.factor}, {self.units_to}, {self.units_from}'

# con 객체 생성
if __name__ == '__main__':
    con = ScaleConverter('KB', 'MB', 1024)

    print(con)
    print("1MB를 변환하기")
    # print(str(con.convert(2)) + con.units_to)
    print(f'1{con.units_from} = {con.convert(1)}{con.units_to}')

    con2 = ScaleConverter('inch', 'mm', 25.4)
    print(f'2{con2.units_from} = {con2.convert(2)}{con2.units_to}')