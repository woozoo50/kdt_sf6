# 클래스 샘플
from tkinter import *

def click():
    result = value.get()  # value = 10 > result
    text.delete(0.0, END)  # 기존거 지우고 insert
    text.insert(END, result)  # result (=value) 값 표시

# 실행 영역
root = Tk()
root.title("정수형 변수")
root.geometry("200x100")

# 윈도우 정수형 객체 선언
value = IntVar()
value.set(10)

Button(root, text="확인", command=click).grid(row=0, column=0)

text = Text(root, width=10, height=2)
text.grid(row=1, column=0)

root.mainloop()