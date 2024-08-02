msg = "Have a nice day!"
print(msg[0])
print(msg[-1])
print(msg[0:4])

#nice day!
print(msg[7:])

#문자열 포맷 서식
# %d-정수 , %s-문자열 , %f-실수
print("나는 이번 달에 책을 %d권 샀어요" % 2)
print("나는 이번 달에 책을 %s권 샀어요" % '두')

#변수 대응 , 변수 두 개 이상일 시 괄호로 묶음
count = 2
print("나는 이번 달에 책을 %d권 샀어요" % count)
cost = 50000
print("나는 이번 달에 책을 %d권 샀고, 비용은 %d원 들었어요" % (count, cost))

#1인치 - 2.54cm
print("1인치는 %.2fcm 입니다." % 2.54)

#f 포맷 방식
print(f'나는 이번 달에 책을 {count}권 샀고, 비용은 {cost}원 들었어요')

unit = 2.540000
print(f'1인치는{unit : .2f}cm 입니다.')
