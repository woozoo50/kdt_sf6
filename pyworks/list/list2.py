
score = [10, 20, 30, 40, 80]

print(score)

print(score[2])

# 요소 수정
score[1] = 50
print(score)

# 요소 삭제
del score[2]
print(score)

score2 = [10, 20, 30, 40, 50]
#인덱싱 : 특정한 한개 요소에 접근
print(score2[2])

#슬라이싱 : 여러개 요소에 접근(콜론(:) 사용, 최종값 -1한 인덱스가 출력)
print(score2[0:3]) #처음부터 2번까지 접근
print(score2[:3])
print(score2[3:])
print(score2[:])