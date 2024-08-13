import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple', 'mountain', 'garlic', 'onion', 'potato']

n = 1  # 문제 번호 (1 ~ 10)
input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n < 11:
    print("문제", n)
    question = random.choice(word)
    print(question) # 단어 출제
    user = input()  # 유저가 단어 입력
    if user == question:
        print("통과!!")
        n = n + 1
    else:
        print("오타!, 다시 도전!")

end = time.time()
et = end - start
print("프로그램 종료")
print(f'타자 시간 : {et : .2f}초')