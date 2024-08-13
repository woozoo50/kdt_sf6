# 실습 1

#(1)
while True:
    try:
        num = int(input("숫자 입력 : "))
        break
    except ValueError:
        print('정수가 아님! 정수를 입력해주세요!')

print(f'정수 입력 성공 : {num}')

#(2)
while True:
    try:
        num = int(input("숫자 입력 : "))
    except ValueError:
        print('정수가 아님! 정수를 입력해주세요!')
    else:
        print(f'정수 입력 성공 : {num}')
        break