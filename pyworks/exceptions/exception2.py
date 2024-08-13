# try ~ except ~ finally

def divide(x, y):
    try:
        # 실행되는 구간(예외가 발생할 수 있음)
        result = x / y
        print(result)
    except ZeroDivisionError:
        print("0으로 나눌 수 없음")
    finally:
        print("여기는 반드시 수행됩니다.")

divide(2, 3)
divide(2, 0)
