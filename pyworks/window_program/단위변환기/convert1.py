# KB - MB 변환
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
        kb = self.kb.get()
        conv_mb = self.conv.convert(kb)
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
root.title("정수형 변수")
root.geometry("250x100+200+200")

app = App(root)

root.mainloop()