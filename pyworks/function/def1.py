# print("Hello~")
# 인사하는 함수 - greet
# 재사용이 가능한 코드 조각

def greet():
    print("안녕~")

def greeting(name):
    print("안녕~", name)

greet() #호출

greeting("현수") #name = "현수"

def get_gugu(dan):
    for i in range(1,10):
        print(f'{dan} * {i} = {dan * i}')

get_gugu(2)

def add(x, y):
    total = x + y
    print("더하기 : ", total)

add(3,5)

def square(x):
    return  x * x

val = square(6)
print(val)
print(square(7))

# 절대값 구하는 감수 -abs(x)
print(abs(-10))
print(abs(10))

def myabs(x):
    if x < 0:
        return -x
    else:
        return x

print(myabs(-10))
print(abs(10))

def mul(x, y):
    return x * y

print(mul(5, 3))
value2 = mul(3, 6)
print(value2)


