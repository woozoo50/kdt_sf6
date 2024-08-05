#다중 if 실습
score = int(input("점수를 입력하세요 : "))
grade = "" #빈 문자열

if score > 100 or score <0:
    print("0~100 사이 숫자 입력")
elif score >= 90 and score <=100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f'{grade}등급 입니다.')