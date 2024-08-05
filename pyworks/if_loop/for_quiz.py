#실습 1
num = int(input("어디까지 계산할까요?"))
total = 0
for i in range(1,num+1):
    total += i
print(total)

#실습 1-1 홀수합계
num = int(input("어디까지 계산할까요?"))
total = 0
for i in range(1,num+1):
    if i % 2 !=0:
        total += i
print(total)


#실습 2
count = int(input("몇 초? : "))
for i in range(count, 0, -1):
    print(i, end=" ")
print("발사!!")
