# 반올림 - round(숫자, 자리수)
#         0 : 정수 / 1 : 소수점 첫째 , 2 : 소수점 둘째 ... / -1 : 일의 자리 , -2 : 십의 자리 ...

round_v1 = round(2.547, 0)
print(round_v1)

round_v2 = round(2.547, 1)
print(round_v2)

round_v3 = round(1275, -1) #0자리
print(round_v3)

# 문자열 표현 수식을 숫자로 변환 - eval('문자')
eval_v = eval('1+2')
print(eval_v)