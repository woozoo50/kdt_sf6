# 별찍기
floor = int(input("몇 줄? : "))

for i in range(1, floor+1):
    print("*" * i)

print("="*20)

# 공백이 먼저인 직각삼각형
for i in range(1, floor+1):
    print(" " * (floor+1-i) + "*" * i)

print("="*20)

# 정삼각형
for i in range (1, floor+1):
    print(" " * (floor+1-i) + "*" * (i*2-1))

"""
n1 = int(input("몇 줄? : "))
for i in range(0, n1):
    for j in range(1, n1 - i):
        print(" ", end="")
    for j in range(1, 2 * i + 2):
        print("*", end="")
    print() #행바꿈
"""
