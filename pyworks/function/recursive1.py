# 재귀함수 - 자기 자신을 호출하는 함수

def sos(n):
    print("Help me !!")
    if n==1:  #종료 조건
        return ""
    else:
        return sos(n-1)

sos(3)

'''
 sos(3)
 n=3, Help me!
  > sos(2)
    n=2, Help me!
    > sos(1)
    n=1, Help me! 
    > return("")
'''

# 팩토리얼 계산
def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(4))
