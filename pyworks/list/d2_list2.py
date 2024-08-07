
a = [1, 2, 3, 4]

total = 0
for i in a:
    total += i
print(total)

print("합계 : ", total)
print("평균 : ", total / len(a))

#2차원 리스트의 합계와 평균
d = [
    [1],
    [2, 3],
    [4, 5, 6]
]

sum_v = 0
count = 0
for i in range(len(d)):
    for j in range(len(d[i])):
        sum_v = sum_v + d[i][j]
        count += 1  #count++ 안됨

print("요소의 개수 : ", count)
print("합계 : ", sum_v)
print("평균 : ", sum_v / count)