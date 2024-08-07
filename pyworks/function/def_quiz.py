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

#print(f'상품1 가격 : {format(order1, '.d')}원')