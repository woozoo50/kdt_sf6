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


