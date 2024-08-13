# 숫자 추측 게임 - 1~100
import  random

# 컴의 랜덤값
com = random.randint(1,100)

min_v = 1
max_v = 100

point = 100

while True:
    try:
        # 서식 대응 문자 - %d , %f , %s
        guess = int(input("숫자 입력 (%d ~ %d) : " % (min_v, max_v)))

        if guess <0 or guess > 100:
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답")
            break
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
            point -= 10
        elif com < guess:
            print("랜덤수보다 커요")
            max_v = guess
            point -= 10

    except ValueError:
        print("숫자만 입력해 주세요.")

print(point)