# 변수의 유효 범위
# 전역 변수 - 전체에 영향을 미침
# 지역 변수 - 함수나 제어문 내에서만 생성 소멸

# 상품 가격 = 단위당 가격 * 수량
def get_price():
    price = 4000 * quantity
    return price

quantity = 2  # 전역 변수 --> 지역 변수에 값을 줌
order_price = get_price()
print(f'{order_price}')
# print(f'{price}') 지역 변수 > 전역 변수 x


def get_price():
    price = 4000 * quantity
    return price

def one_up():
    x = 0  # 지역변수 , 값을 반환하고 소멸
    x += 1
    return x

print(one_up())
print(one_up())
# print(x)

