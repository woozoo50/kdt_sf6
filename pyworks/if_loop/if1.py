
# if문 - 조건 : 나이가 15세 이상이면 "관람가" 출력
# 구문 만들때 끝에 콜론(:)을 붙이고 다음줄에서 들여쓰기(인덴트)

age = 10

'''
#if 문
if age >= 15:
    print("관람가")
print(f'나이는 {age}세 입니다.')
'''

#if ~ else문 : 조건이 True이면 if문 실행하고, 조건이 False 이면 else문을 실행
if age >= 15:
    print("관람가")
else:
    print("관림불가")
print(f'나이는 {age}세 입니다.')

#어떤 수를 짝수인지 홀수인지 판단하는 프로그램
num = int(input("수를 입력 하세요 : "))

if num % 2 == 0 :
    print("짝수")
if num % 2 == 1 :
    print("홀수")

print(f'입력된 수는 {num}입니다.')