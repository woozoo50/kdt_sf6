# if ~ if 구문과 if ~ elif 구문의 차이
# elif는 가장 위에서 참인 값이 실행 되고 프로그램이 종료
# if ~ if 는 참인 값은 모두 실행됨

str = ("Life is short, You need Python")

if "Wife" in str: # False
    print("Wife")
elif "Life" in str and "Python" not in str:  # False
    print("Life")
elif "good" not in str:  # Ture
    print("good")
elif "need" in str:  # Ture 이지만 실행되지 않음
    print("need")
else:
    print("none")
    

if "Wife" in str: # False
    print("Wife")
if "Life" in str and "Python" not in str:  # False
    print("Life")
if "good" not in str:  # Ture
    print("good")
if "need" in str:  # Ture
    print("need")
else:
    print("none")