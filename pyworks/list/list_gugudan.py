# 구구단 프로그램 구현 -리스트

dan = 2
gugu = [] #구구단의 결과값 저장 (2, 4, 6, 8...)
for i in range(1, 10):
    gugu.append(dan * i)
    print(f'{dan} * {i} = {gugu[i-1]} ')
print("=================================================")

# 구구단 전체 출력
for i in range(2, 10):
    row = []
    for j in range(1, 10):
        row.append(i * j)
        print(f'{i} * {j} = {row[j-1]}')
    # print(row)
    print("====================================")