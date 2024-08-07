# 학생 5명의 국어, 수학 총점과 평균

score = [
    [80, 70],
    [70, 95],
    [60, 90],
    [50, 75],
    [75, 60]
]

# 개인별 총점과 평균
# 개인별 총점을 저장
total = 0
students = [] # 총점 저장

n = len(score)
for i in range(0, n):
    total = score[i][0] + score[i][1]
    # total(지역변수)는 필요한 곳에서 선언해서 사용
    # 지역변수는 코드블럭을 빠져나올때 소멸
    students.append(total)

    # 과목별 총점과 평균
    print(total)
    print(total / 2)

print(students)

# 과목 별 총점과 평균
# 국어 총점, 수학 총점, 국어 평균, 수학 평균
sum_subject = [0, 0] # 국어 총점, 수학 총점
avg_subject = [0.0, 0.0] # 국어 평균, 수학 평균

for i in range(0, n):
    sum_subject[0] += score[i][0]
    sum_subject[1] += score[i][1]

# 평균 계산
avg_subject[0] = sum_subject[0] / n
avg_subject[1] = sum_subject[1] / n

print("국어 총점 : " , sum_subject[0])
print("수학 총점 : " , sum_subject[1])
print("국어 평균 : " , avg_subject[0])
print("수학 평균 : " , avg_subject[1])
