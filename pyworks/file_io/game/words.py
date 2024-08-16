# 영어 단어장 만들기
# 경로 - game 폴더에 위치함
import random

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple', 'mountain', 'garlic', 'onion', 'potato']

try:
    with open('./words.txt', 'w') as f:
        for i in word:
            f.write(i + " ")

except:
    print("파일을 찾을 수 없습니다.")

# 단어 읽기 , 랜덤으로 추출
try:
    with open("./words.txt",'r') as f:
        data = f.read().split()  # 공백 문자로 구분(리스트로 반환)
        # print(data)
        word_choice = random.choice(data)  # 랜덤으로 리스트에서 1개 선택
        print(word_choice)

except:
    print("파일을 찾을 수 없습니다.")