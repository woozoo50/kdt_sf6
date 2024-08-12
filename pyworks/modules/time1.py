# time 모듈
# time.time() 자정 이후부터 시간을 초로 변환
import time
import math

print(time.time())

# 일 / 년 환산
day = math.floor(time.time() / (24 * 60 * 60))
year = math.floor(time.time() / (365 * 24 * 60 * 60))

print(day)
print(year)

# time.sleep(n) - n초 간격으로 대기
for i in range(1, 11):
    print(i)
    #time.sleep(1)

# 수행(실행) 시간 측정
start = time.time()
for i in range(1, 1000000):
    print(i)
    #time.sleep(1)
end = time.time()
print("수행시간 : " + str(end-start) + "초")

