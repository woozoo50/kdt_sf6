import datetime
# 날짜와 시간 모두 출력
now1 = datetime.datetime.now()
now2 = datetime.datetime.today()

print(now1)
print(now2)

print(now1.year)
print(now1.month)
print(now1.day)

# 날짜만 출력
print(f'{now1.year}-{now1.month}-{now1.day}')

# 시간만 출력
print(f'{now1.hour}:{now1.minute}:{now1.second}')

# 2023년 7월 31일 출력
the_day = datetime.date(2023, 7, 31)
print(the_day)

# 오늘 날짜만 출력
today = datetime.date.today()
print(today)

print("★ 지금까지 몇 일? ★")
passed_time = today - the_day
print(f' 개강 이후 {passed_time.days}일 지났습니다')

# 추석까지 D-Day 사용해서 구현
holiday = datetime.date(2024, 9 ,17)
d_day = holiday - today
print(f'추석까지 {d_day.days}일 남았습니다.')