# random 모듈
import random
import math

# 무작위 수 출력 (0.0 <= r < 1)
print(random.random())

# 주사위 - 방법1
dice = random.randint(1,6)
print(dice)

# 주사위 - 방법2
dice2 = random.random() * 6 + 1
print(dice2)
dice2 = math.floor(dice2)
print(dice2)

# 주사위 10번 던지기
dice_re = []

for i in range(10):
    dice2 = random.random() * 6 + 1
    dice2 = math.floor(dice2)
    dice_re.append(dice2)

print(dice_re)

# 랜덤하게 단어 추출하기 - 방법1
words = ['여름', '꽃', '나비', '벌', '나무']
print(random.choice(words))

# 랜덤하게 단어 추출하기 - 방법2
idx = math.floor(random.random() * len(words))
print(words[idx])
