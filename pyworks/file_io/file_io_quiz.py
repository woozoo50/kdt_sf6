# 실습 1
"""
# 쓰기

f = open("c:/pyfile/gugudan.txt", "w")

for i in range(2,10):
    for j in range(1, 10):
        gugudan = f'{i} * {j} = {i * j}\n'
        f.write(gugudan)
    f.write("=============================\n")

f.close()

# 읽기

f = open("c:/pyfile/gugudan.txt", "r")

data = f.read()
print(data)

f.close()
"""

#실습 2

try:
    with open("./source/member.txt", 'w') as f:
        for i in range(1,4):
            user_id = input(f"{i}번째 회원 아이디 : ")
            user_pw = input(f"{i}번째 회원 비밀번호 : ")
            f.write(f'{user_id} {user_pw}\n')

    with open("./source/member.txt", "r") as f:
        print(f.read())

except:
    print("파일을 찾을 수 없습니다.")


#실습 3

name = input('이름 입력 : ')
pw = input('비밀번호 입력 : ')
user = name + " " + pw + "\n"

with open("./source/member.txt", "r") as f:
    member_list = f.readlines()  # 데이터를 리스트로 반환
    print(member_list)

# 상태 변수 - True / False
sw = False  # 상태 초기화 False임
for member in member_list:  #리스트를 순회하면서
    if member == user:  # 파일에 있는 member의 name, pw와 입력한 user의 name과 pw가 일치하면
        sw = True  # 상태 변수를 Ture로 저장

if sw == True:
    print("로그인 성공!")
else:
    print("로그인 실패!")


