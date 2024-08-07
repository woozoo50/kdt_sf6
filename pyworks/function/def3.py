# 1부터 n까지 곱하는 함수
def gob_n(n):
    gob_v =1
    for i in range(1, n+1):
        gob_v *= i

    return gob_v

print (gob_n(4))
