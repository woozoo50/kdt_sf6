# 실습 1

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
