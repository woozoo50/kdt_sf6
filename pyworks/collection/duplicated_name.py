# list , set을 사용 - 중복 이름 찾기

name = ["흥부", "콩쥐", "놀부", "콩쥐"]

#duplicated_name = set() #빈 셋을 생성
duplicated_name = [] #빈 리스트를 생성
n = len(name)

for i in range(0, n-1):   # n=4
    for j in range(i+1, n):
        if name[i] == name[j]:
            # duplicated_name.add(name[i]) #셋
            duplicated_name.append(name[i]) #리스트


"""
 i=0 , j=1 : name[0] == name[1]?
 i=0 , j=2 : name[0] == name[2]?
 i=0 , j=3 : name[0] == name[3]?
 i=1 , j=2 : name[1] == name[2]?
 i=1 , j=3 : name[1] == name[3]?
 i=2 , j=3 : name[2] == name[3]?
"""

print(f'중복 이름 : {duplicated_name}')
