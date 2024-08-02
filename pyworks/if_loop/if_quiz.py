# 실습 1

# 조건 - 시내에서 자동차의 주행 속도가 50km/h 이상이면 "속도 위반입니다" 출력하고
# 아니면 "규정 속도 준수!!"를 출력하세요

current_speed = float(input("주행 속도를 입력하세요. : "))

if current_speed >= 50 :
    print("속도 위반입니다. 과태료 10만원 부과")
else :
    print("규정 속도 준수!!")
print(f'주행 속도는 {current_speed}km 입니다.')