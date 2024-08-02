#입력함수 - input(문자열)

name = input("이름 입력 : ")

print(f'당신의 이름은 {name} 이군요')

number = input("숫자 입력 : ")

print(f'{number}')
print(int(number) + 1)

'''
#오류 처리 (try ~ except)
try :
    실행문 (오류가 나올 수 있는 문)
except :
    오류를 처리 할 수 있는 구문

# :(콜론) - 코드 블럭 {} - 다음 줄에서는 들여쓰기
'''

try : 
    num1 = int(input("첫 번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))
    print(num1 + num2)
except :
    print("정수를 입력해주세요")
