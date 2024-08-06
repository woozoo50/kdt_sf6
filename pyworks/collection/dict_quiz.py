# 실습1
dict1 = {}

dict1["Alice"] = 85
dict1["Bob"] = 90
dict1["Charlie"] = 95
dict1["David"] = 80

dict1["Alice"] = 88

dict1.pop("Bob")

for key in dict1:
    print(key , ":", dict1[key])

for key in dict1.keys():
    print(f"{key}의 점수는 {dict1.get(key)}")



#실습2
dict2 = [
    {"name" : "이대한", "kor" : 90 , "math" : 85},
    {"name" : "박민국", "kor" : 80 , "math" : 75},
    {"name" : "임지능", "kor" : 95 , "math" : 90}
]