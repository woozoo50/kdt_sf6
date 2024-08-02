"""

변수 선언(변수명 문법)
 - 숫자로 시작하면 안됨
 - 공백문자가 있으면 안됨
 - 특수문자 불가능('_' 가능)

에러
 - 실행 전 에러(컴파일 오류)
 - 실행 후 에러(런타임 에러)
 
"""

season = "여름"


print(season)

print('*** 회원가입 ***')
user_id = "kdt6"
user_pw = "sf1234"
email = "woozoo50@naver.com"
age = 35

print("아이디 :", user_id)
print(f'아이디 : {user_id}')
print("비밀번호 :", user_pw)
print("이메일 :", email)
print("나이 :", age)

#소수점 처리하기
#int , float
n1 = 10
n2 = 3
div = n1/n2
print(div)
print(type(n1))
print(type(div))
print(f'결과값 : {div}')
print(f'결과값 : {div : .1f}')
print(f'결과값 : {round(div, 2)}')

# 반올림 함수 - Round(숫자 , 자리수)
print(round(1.643))
print(round(1.643, 2))

# 실습 - 빵 30 , 사람 4명
bread = 30
people = 4

몫 = bread // people
나머지 = bread % people

print("빵의 개수 : " + str(몫))
print("남은 빵의 개수 : " + str(나머지))

