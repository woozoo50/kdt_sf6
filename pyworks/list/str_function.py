'''
유용한 문자열 함수
-개수 : len()
-특정한 문자 개수 : 문자열.count("찾을 문자")
-대문자 변환 : 문자열.upper()
-소문자 변환 : 문자열.lower()
-문자열을 잘라서 리스트로 반환 문자열.split("구분자")
-특정한 문자를 변경 - replace(old ,new)
'''

f = "banana"
print(len(f))

dupl_count = "banana"
print(dupl_count.count("a")) #a 갯수 3개 출력
print(dupl_count.count("z")) #z 갯수 0개 출력

upper_case = "Hello".upper()
lower_case = "Hello".lower()
print(upper_case, lower_case)

friends = ("존 루나 제리")
print(friends.split(" "))
friends = ("존/루나/제리")
print(friends.split("/"))

email = "codingOn@spreatics.com"
print(email.split("@"))

msg = "Hello Python"
print(msg.replace("Python", "C++"))

#입력받아서 리스트 만들기
input_num = input("숫자 입력 : ").split(" ")
print(input_num)
numbers = []
for i in input_num:
    numbers.append(int(i))
print(numbers)

alpha = "a:b:c:d"
