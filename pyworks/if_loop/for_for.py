# 중첩 for
for i in range(1, 5):
    for j in range(1, 5):
        print("*", end='')
    print() #행바꿈

# 중첩 for
for i in range(1, 5):
    for j in range(1, i+1):
        print("*", end='')
    print() #행바꿈

# 중첩 for2
for i in range(1, 5):
    for j in range(1, 6 - i):
        print("*", end='')
    print() #행바꿈

print("===========================================")


# 파이썬의 단일 for
for i in range(1,5):
    print("*" * i)

for i in range(1,5):
    print("*" * (5-i))

for i in range (1,5):
    print(" " * (4-i) + "*"*i)

#숫자가 연속으로 증가하는 알고리즘
for i in range(0,4):
    for j in range(1,5):
        num = i * 4 + j
        if num >= 16:
            break
        print(num, end=' ')
    print()


"""
# 실습 5
n1 = int(input("몇 층? : "))
for i in range(0, n1):
    for j in range(1, n1 - i):
        print(" ", end="")
    for j in range(1, 2 * i + 2):
        print("*", end="")
    print() #행바꿈

for i in range (0, n1):
    print(" " * (n1-1-i) + "*" * (i*2+1))
"""