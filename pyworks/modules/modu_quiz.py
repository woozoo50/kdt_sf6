# 실습1
import random

for i in range(1,11): # 랜덤 확인을 위해 리스트 10개 Test

    list = [] # 빈 리스트 생성

    for j in range(4): # 4개 숫자 저장
        num_random = random.randint(1, 100) # 1~100까지 중 정수 저장
        list.append(num_random)

    list.sort()
    print(f'{i}번째 리스트 : {list}')