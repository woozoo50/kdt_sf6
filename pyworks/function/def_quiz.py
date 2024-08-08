"""
# 실습 1

def quiz(x, y):
    if x == y:
        print(f'결과(곱) : {x * y}')
        return x * y

    else:
        print(f'결과(합) : {x + y}')
        return x + y

result1 = quiz(2,2)
result2 = quiz(2,3)

print(result1)
print(result2)

print("============================================")

# 실습 2
def get_price(x,y):
    total = 0
    if x * y >= 20000:
        total = x * y
        return total
    else:
        total = x * y + 2500
        return total

order1 = get_price(10000,3)
order2 = get_price(5000,3)

print(f'상품1 가격 : {order1}원')
print(f'상품2 가격 : {order2}원')

print(f'상품1 가격 : {format(order1,',d')}원')

print("============================================")

# 실습 4
def get_number(mul):
    count = 0
    for i in range(1,31):
        if i % mul == 0:
            print(f'{i}', end=" ")
            count += 1
    print("")
    '\n-줄바꿈, \t-탭'
    print(f'\n{mul}의 배수의 개수 : {count}')

get_number(3)
get_number(4)
get_number(5)

"""
# 실습 3
def check_machine(check):
    print("남은 음료는", check)

def is_drink(drink, check):
    if drink in check:
        return 1
    else:
        return 0

def add_drink(drink):
    vending_machine.append(drink)
    vending_machine.sort()

def remove_drink(drink):
    vending_machine.remove(drink)
    vending_machine.sort()

vending_machine = ['게토레이', '레쓰비', '생수', '이프로', '게토레이','이프로', '생수']

while True:
    print("====================RESTART")
    who = input("사용자 종류를 입력하세요 : \n1.소비자 \n2.주인\n")

    if who == '1':
        drink = input("마시고 싶은 음료? : ")
        check = is_drink(drink, vending_machine)
        if check == 1:
            remove_drink(drink)
            print(drink, "드릴게요")
            check_machine(vending_machine)
        else:
            print(f'{drink}는 지금 없네요')

    elif who == '2':
        todo = input("할 일 선택(1.추가 , 2.삭제) : ")
        if todo == '1':
            drink = input("추가할 음료수 : ")
            add_drink(drink)
            print("추가 완료")
            check_machine(vending_machine)

        elif todo == '2':
            drink = input("삭제할 음료수 : ")
            check = is_drink(drink, vending_machine)
            if check == 1:
                remove_drink(drink)
                print("삭제 완료")
                check_machine(vending_machine)
            else:
                print(f'{drink}는 지금 없네요')

