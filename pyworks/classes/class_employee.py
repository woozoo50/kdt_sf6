# 사원의 사번을 자동 부여

class Employee:
    serial_num = 1000
    def __init__(self, name):
        self.name = name
        Employee.serial_num += 1  # 시리얼 번호를 1 증가
        self.id = Employee.serial_num

    # __str__() : 객체 정보를 출력하는 매서드
    def __str__(self):
        return "이름 : {} / 사번 : {}".format(self.name, self.id)


emp1 = Employee("최사원")
print(emp1.__str__())
print(emp1)

emp2 = Employee("정사원")
print(emp2)

emp3 = Employee("박사원")
print(emp3)