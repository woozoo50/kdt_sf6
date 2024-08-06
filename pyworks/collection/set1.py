# 자료구조 - set - {}
# 중복이 안됨, 순서가 없다(인덱싱 안됨)

cart = ["양파", "쌀", "콩나물", "쌀", "양파"]
print(cart)

cart2 = {"양파", "쌀", "콩나물", "쌀", "양파"}
print(cart2) #순서 랜덤
#print(cart2[0]) #'set' object is not subscriptable

# 빈 집합(set) 생성
s1 = set() #set() 함수 사용
print(s1)

print('a' in s1) #True
print('d' in s1) #False

# 요소 추가
s1.add('a')
s1.add('b')
s1.add('c')
print(s1) #{'c', 'b', 'a'}

# 요소 삭제
s1.remove('b')
print(s1) #{'c', 'a'}

# 모든 요소 삭제
s1.clear()
print(s1)

#중복 제거
a = [1, 2, 2, 3, 3, 3]
print(set(a))
print(list(set(a)))