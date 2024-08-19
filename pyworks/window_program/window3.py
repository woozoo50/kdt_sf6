from tkinter import *

def click():
    # print("안녕~ 파이썬!")
    label.config(text="안녕~ 파이썬!")

# 루트
root = Tk()
root.title("윈도우3")
# 창크기(가로x세로)
root.geometry("300x150")  # 창크기
root.option_add('*Font', "맑은고딕 15")

'''
Label(root, text="Hello~ Python!!").grid(row=0, column=0)
# command 속성 : 버튼 눌렀을 때 함수를 실행(click)
# 함수 생성 시점이 아닌 클릭했을때 실행되어야 해서 괄호를 뺀다
Button(root, text="확인", command=click).grid(row=1, column=0)
'''

# 프레임
frame = Frame(root)
frame.pack()

Label(frame, text="Hello~ Python!!").grid(row=0, column=0)
# command 속성 : 버튼 눌렀을 때 함수를 실행(click)
# 함수 생성 시점이 아닌 클릭했을때 실행되어야 해서 괄호를 뺀다
Button(frame, text="확인", command=click).grid(row=1, column=0)
# 출력 레이블
label = Label(frame, text=" ")
label.grid(row=2, column=0)

root.mainloop()
