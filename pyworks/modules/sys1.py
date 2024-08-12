# 명령행(command Line)에서 인수 전달하기
import sys

print(sys.argv)

# python sys1.py cat dog cow

args = sys.argv[1:] #0번 제외 - 파일 이름

print(args)

#입력값의 합계와 평균 계싼
total = 0
for i in args:
    total += int(i)

print("합계 : ", total)
print("평균 : ", total / len(args))