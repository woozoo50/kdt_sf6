# global - 전역변수임을 알려주는 키워드
# 전역변수는

def one_up():
    global x
    x += 1
    return x

x = 0
y = 2
print(one_up())
print(one_up())
print(one_up())



