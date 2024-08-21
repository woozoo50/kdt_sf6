class Scale_converter:
    def __init__(self, unit_from, unit_to, factor):
        self.units_from = unit_from
        self.units_to = unit_to
        self.factor = factor

    def convert(self, value):
        return value / self.factor

if __name__ == "__main__":
    con2 = Scale_converter('KB', 'MB', 1024)
    print("*** KB를 MB로 변환 ***")
    print(f'{con2.convert(1630) : .2f}{con2.units_to}')