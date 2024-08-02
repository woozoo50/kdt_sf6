# 리스트 함수

# 추가 - 리스트.append(), 리스트.insert()
# 삭제 - 리스트.pop(), 리스트.remove()
# 정렬 - 리스트.sort()
# 뒤집기 - reverse()

lower = ['b', 'd', 'a', 'c']

#정렬(오름차순)
lower.sort()
print(lower)
lower.reverse()
print(lower)

'''
lower.append('e') #맨 뒤에 추가됨
print(lower) #맨 뒤에 추가됨

lower.pop() #맨 뒤에 삭제
print(lower) #맨 뒤에 삭제

lower.insert(2, 'e')
print(lower)

lower.remove('c')
print(lower)

lower2 = ['a', 'c', 'd', 'c']
lower2.remove('c')
print(lower2)
'''