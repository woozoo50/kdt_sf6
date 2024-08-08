# 가변 매개변수
# 매개변수의 입력값이 정해지지 않고 변경해야 할 때 사용하는 변수이다.
# 변수이름 앞에 *을 붙인다.

def calc_avg(*numbers):  #[1, 2.....]
    sum_v = 0
    for i in numbers:
        sum_v += i
    re = sum_v / len(numbers)
    return re


avg1 = calc_avg(1,2)
print(avg1)

avg2 = calc_avg(1,2,3,4)
print(avg2)