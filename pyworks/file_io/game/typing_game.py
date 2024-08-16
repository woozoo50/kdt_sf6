import random
import time

# 메모장 파일 읽어오기
try:
    with open("./words.txt",'r') as f:
        word = f.read().split()  # 공백 문자로 구분(리스트로 반환)
        # print(data)
        # word_choice = random.choice(word)  # 랜덤으로 리스트에서 1개 선택
        # print(word_choice)
except:
    print("파일을 찾을 수 없습니다.")

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