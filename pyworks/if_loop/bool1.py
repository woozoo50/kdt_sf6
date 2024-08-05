# 비교 연산 : > , >= , < , <= , == , !=
# 비교 연산의 결과는 - bool자료 (T/F)

b1 = 2 > 1
print(b1) #True
print(type(b1))

b2 = 2==1
print(b2) #False
print(type(b2))

b3 = 2!=1
print(b3) #True
print(type(b3))

# 논리 연산 : and , or , not
# and : 두 가지 이상 조건에서 모두 참일 때만 참
# or : 두 가지 이상 조건에서 둘 중 하나라도 참이면 참
# not :
logic1 = (2 > 1) and (2 == 1)
print(logic1)
print(type(logic1))

logic2 = (2 > 1) or (2 == 1)
print(logic2)
print(type(logic2))

logic3 = not (2 != 1)
print(logic3)
print(type(logic3))

# 논리 연산 예제
age = 17
under_20 = age < 20
print(under_20)
print(not under_20)

#논리곱
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#논리합
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#논리 부정
print(not True)
print(not False)