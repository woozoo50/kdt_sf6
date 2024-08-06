# 실습 4

age = int(input("나이를 숫자로 입력해 주세요: "))
sel = input("결제 방법을 입력해주세요(카드 또는 현금만 입력): ")
fee = 0
if age >=0 and ((sel == "카드") or (sel == "현금")):
    if age < 8 or age >= 75:
        fee = 0
    elif age < 14:
        fee = 450
    elif age < 20:
        if sel == "카드":
            fee = 720
        elif sel == "현금":
            fee = 1000
        else:
            print("올바른 결제 방법을 입력해주세요")
    else:
        if sel == "카드":
            fee = 1200
        elif sel == "현금":
            fee = 1300
        else:
            print("올바른 결제 방법을 입력해주세요")
    print(f'{age}세의 {sel}요금은 {fee}원입니다.')
else:
    print("올바른 나이 또는 결제 방법을 입력해 주세요")