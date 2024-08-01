# 실습1

try :
    name = input("이름을 입력하세요 : ")
    age = int(input("나이를 입력하세요 : "))

    print(f'안녕하세요! {name}님 ({age}세)')

except ValueError: 
    print("정수를 입력해주세요")

    

# 실습2

try :
    name = input("이름을 입력하세요 : ")
    year_birth = int(input("태어난 년도를 입력하세요 : "))
    year_this = int(input("올해 년도를 입력하세요 : "))
    age = year_this - year_birth + 1
    print(f'올해는 {year_this}년, {name}님의 나이는 {age}세 입니다.')
except ValueError: 
    print("정수를 입력해주세요")
