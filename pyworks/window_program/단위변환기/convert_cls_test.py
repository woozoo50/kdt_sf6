# 클래스 샘플
from tkinter import *

class App:
    def __init__(self, root):
        self.conv = ScaleConverter('KB', 'MB', 1024)
        frame = Frame(root)
        frame.pack()

        Label(frame, text="KB").grid(row=0, column=0)
        self.kb = IntVar()
        Entry(frame, textvariable=self.kb).grid(row=0, column=1)

        Label(frame, text="MB").grid(row=1, column=0)
        self.mb = DoubleVar()
        Label(frame, textvariable=self.mb).grid(row=1, column=1)

        Button(frame, text="변환", command=self.convert).grid(row=2, column=2)

    def convert(self):
        kb = self.kb.get()   # 사용자가 입력한 값을 kb 변수에 저장
        conv_mb = self.conv.convert(kb)  # 입력값을 factor(1024)로 나눔
        conv_mb = f'{conv_mb: .2f}'
        self.mb.set(conv_mb)


class ScaleConverter:
    def __init__(self, unit_from, unit_to, factor):
        self.units_from = unit_from
        self.units_to = unit_to
        self.factor = factor

    def convert(self, value):
        return value / self.factor


# 실행 영역
root = Tk()
root.title("단위 변환기")
root.geometry("300x150+200+200")

app = App(root)

root.mainloop()