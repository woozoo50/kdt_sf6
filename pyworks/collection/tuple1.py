# 튜플 (tuple) - 소괄호, 읽기 전용(수정, 삭제 안됨)

t1 = (10, 20, 30)

print(t1)
print(type(t1))

# 요소 접근 - 읽기(검색) 가능
print(t1[0]) #10
print(t1[1:4]) #(20, 30)
print(t1[-1]) #30

# 수정 불가능
# t1[1] = 50

# 삭제 불가능
#del t1[1]
#t1.remove(10)

#요소를 1개 생성할때 쉼표를 넣어줌
t2 = (7)
print(t2)
print(type(t2)) #int

t3 = (7, )
print(t3)
print(type(t3)) #tuple

# 튜플 요소의 합계
print(sum((10, 20, 30))) #60

# 튜플 요소의 최소값 , 최대값
print(min((10, 20, 30))) #10
print(max((10, 20, 30))) #30

#튜플 합하기
tu1 = (1, 2, 3)
tu2 = (4, 5, 6)

tu3 = tu1 + tu2 #(1, 2, 3, 4, 5, 6)
print(tu3)
