#다중 조건문
'''
if 조건1 :
    실행문 (조건 1 참일때)
elif 조건2 :
    실행문 (조건 2 참일때)
else 조건3 :
    실행문 (조건 1,2 모두 거짓일떄)
'''

age = 25
if age < 20 :
    print("미성년자 입니다.")
elif age < 30 :
    print("20대 입니다.")
elif age < 40 :
    print("30대 입니다.")
else :
    print("이제는 중년")

print(f'나이는 {age}세 입니다.')