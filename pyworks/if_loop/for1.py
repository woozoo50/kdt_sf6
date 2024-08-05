# for 반복분
"""

for i range (시작값, 종료값+1, 증감값):
    실행문
for i in 리스트:
    실행문
"""
# 초기값이 생략되면 0부터 시작
# 끝 값은 실제 (끝값-1) 임

a = range(10)
print(list(a)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = range(1, 11)
print(list(b)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = range(1, 11, 2)
print(list(c)) #[1, 3, 5, 7, 9]

#for문 - 1부터 10까지 출력
for i in range(1,11):
    print(i, end=" ")

#''''''''''
print(" ")

#for문 - 1부터 10까지 합계
total = 0
for i in range(1,11):
    print("i =", i, "total =", total)
    total += i
print(total)


