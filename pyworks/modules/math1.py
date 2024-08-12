# 수학 관련 내장 모듈 - math 사용
import math

print(math.pi)

# 원의 넓이(area)
radius = 6
area = radius * radius * 3.14
area2 = radius * radius * math.pi
print(area)
print(area2)

# 올림
print(math.ceil(2.45))

# 버림
print(math.floor(2.54))

#제곱근
print(math.sqrt(25))

#반올림
print(round(3.14, 1))