# 실습 5
#sum()
# print(sum([1, 2, 3])) #6
#max()
# print(max([1, 2, 3])) #3

#입력받아서 리스트 만들기
input_num = input("숫자 여러 개 입력 > ").split(" ")
numbers = []
for i in input_num:
    numbers.append(int(i))
print(numbers)

print(f'가장 큰 값: {max(numbers)}') #가장 큰 수
print(f'가장 작은 값: {min(numbers)}') #가장 작은 수

numbers.remove(max(numbers)) #가장 큰 값 제거
numbers.remove(min(numbers)) #가장 작은 값 제거

avr_num = sum(numbers) / len(numbers) #나머지 값의 평균

print(f'나머지 값의 평균: {avr_num}')



