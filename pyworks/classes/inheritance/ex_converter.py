# 단위 변환기 확장 클래스
# 클래스의 상속 기능 구현
# F = C * 1.8 + 32

from classes.inheritance.class_scale_converter import ScaleConverter

class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)  # 부모 멤버
        self.offset = offset  # 자기 멤버

    def __str__(self):
        return f'{self.units_to}, {self.units_from}, {self.factor}, {self.offset}'

    def convert(self, value):
        # return super().convert(value) + self.offset
        return value * self.factor + self.offset

conv = Converter('C', 'F', 1.8, 32)
print(conv)
print(f'33{conv.units_from} = {conv.convert(33)}{conv.units_to}')