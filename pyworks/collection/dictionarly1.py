# 자료구조 - 딕셔너리(dictionary)
# "치킨" : "닭을 튀긴 요리", key(키):value(값)
# {} 중괄호 사용

fruits = {
    "apple": "사과",
    "banana": "바나나",
    "peach": "복숭아"
}

# 접근(검색)
print(fruits["apple"])
#print(fruits["tomato"]) #없는 것 검색시 에러

print(fruits.get("banana"))
print(fruits.get("tomato")) #에러 x , #None

#요소 추가
fruits["strawberry"] = "딸기"
print(fruits)
print(type(fruits)) #dict

#요소 수정(변경)
fruits['peach'] = ("천도복숭아") #추가와 같음
print(fruits)

#요소 삭제
fruits.pop("banana")
print(fruits)

# 키 만 반환
print(fruits.keys())

# 값 만 반환
print((fruits.values()))

# 키와 값 모두 반환
print((fruits.items()))

# 키와 값 전체 조회
for key in fruits:
    print(key, ':', fruits[key])  #fruits[key] = Value

# 딕셔너리 생성
dict1 = {1:'a', 2:'b', 3:'c'}
print(dict1)

# key=4, value='d' 추가
dict1[4] = 'd'
print(dict1)

# for문을 이용한 전체 조회
for i in dict1:
    print(f'{i} : {dict1[i]}')

for key in dict1:
    print(f'{key} : {dict1[key]}')

# 요소 수정 - key 3을 'k'로 변경
dict1[3] = 'k'
print(dict1)

# 요소 삭제 - key 2 삭제
dict1.pop(2)
print(dict1)

# 빈 dictionary 생성
dict2 = {}  #set이랑 차이.. s1 = set() #set() 함수 사용