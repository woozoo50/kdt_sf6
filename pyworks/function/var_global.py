# global - 전역변수(정적변수)임을 알려주는 키워드
# 전역변수는 지역변수에 영향을 미침, 프로그램이 종료되면 소멸

def one_up():
    global x
    x += 1
    return x

x = 0
print(one_up())
print(one_up())
print(one_up())


def test1():
    print(num1)
    print(id(num1))
    result = num1 + 10
    return result

num1 = 0
result1 = test1()
print(result1)
print(num1)
print(id(num1))

print("=======================")
def test2():
    num2 = 40
    print(num2)
    print(id(num2))
    num2 = num2 + 20
    return num2

num2 = 0
result2 = test2()
print(result2)
print(num2)
print(id(num2))

print("=======================")
def test3():
    print(num2)
    print(id(num2))
    num2 = num2 + 20 # num2 변경 시에러
    return num2

result3 = test3()