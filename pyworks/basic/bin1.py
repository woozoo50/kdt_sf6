# 진수 표현하기
num = 10 #10진수
b_num = 0b1010 #2진수
h_num = 0xA #16진수

print(num) 
print(b_num)
print(h_num)

#진수 표현 함수
# - bin(숫자) : 2진수로 변환하는 함수
# - hex(숫자) : 16진수로 변환하는 함수

print(bin(num))
print(hex(num))

#아스키 코드값
#ord(문자) - 문자를 코드값으로 변환
#chr(코드값) - 코드값을 문자로 변환

print(ord('0'))
print(chr(48))
print(ord('a'))
print(chr(97))
print(ord('A'))
print(chr(65))
