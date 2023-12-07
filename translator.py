import time
import tkinter.font
from tkinter import *
global position
position = 0 # total words 8
num = 1 # total points
def judge(x):
    global position
    if(position == 8):
        print("error")
        return
    match x:
        case "香":
            w.itemconfigure(1 + position * 12, fill='black')
            w.itemconfigure(3 + position * 12, fill='black')
            w.itemconfigure(4 + position * 12, fill='black')
            w.itemconfigure(5 + position * 12, fill='black')
            w.itemconfigure(6 + position * 12, fill='black')
            w.itemconfigure(11 + position * 12, fill='black')
            w.itemconfigure(12 + position * 12, fill='black')
            w.itemconfigure(97 + position, text = "香")
            position += 1
        case "港":
            w.itemconfigure(1 + position * 12, fill='black')
            w.itemconfigure(2 + position * 12, fill='black')
            w.itemconfigure(5 + position * 12, fill='black')
            w.itemconfigure(6 + position * 12, fill='black')
            w.itemconfigure(7 + position * 12, fill='black')
            w.itemconfigure(11 + position * 12, fill='black')
            w.itemconfigure(12 + position * 12, fill='black')
            w2.itemconfigure(1 + position * 12, fill='green')
            w2.itemconfigure(2 + position * 12, fill='green')
            w2.itemconfigure(5 + position * 12, fill='green')
            w2.itemconfigure(6 + position * 12, fill='green')
            w2.itemconfigure(7 + position * 12, fill='green')
            w2.itemconfigure(11 + position * 12, fill='green')
            w2.itemconfigure(12 + position * 12, fill='green')
            w.itemconfigure(97 + position, text="港")
            position += 1
        case "中":
            w.itemconfigure(2 + position * 12, fill='black')
            w.itemconfigure(7 + position * 12, fill='black')
            w.itemconfigure(8 + position * 12, fill='black')
            w.itemconfigure(9 + position * 12, fill='black')
            w.itemconfigure(12 + position * 12, fill='black')
            w2.itemconfigure(2 + position * 12, fill='green')
            w2.itemconfigure(7 + position * 12, fill='green')
            w2.itemconfigure(8 + position * 12, fill='green')
            w2.itemconfigure(9 + position * 12, fill='green')
            w2.itemconfigure(12 + position * 12, fill='green')
            w.itemconfigure(97 + position, text="中")
            position += 1
        case "文":
            w.itemconfigure(5 + position * 12, fill='black')
            w.itemconfigure(6 + position * 12, fill='black')
            w2.itemconfigure(5 + position * 12, fill='green')
            w2.itemconfigure(6 + position * 12, fill='green')
            w.itemconfigure(97 + position, text="文")
            position += 1
        case "大":
            w.itemconfigure(1 + position * 12, fill='black')
            w.itemconfigure(2 + position * 12, fill='black')
            w.itemconfigure(6 + position * 12, fill='black')
            w.itemconfigure(8 + position * 12, fill='black')
            w.itemconfigure(11 + position * 12, fill='black')
            w2.itemconfigure(1 + position * 12, fill='green')
            w2.itemconfigure(2 + position * 12, fill='green')
            w2.itemconfigure(6 + position * 12, fill='green')
            w2.itemconfigure(8 + position * 12, fill='green')
            w2.itemconfigure(11 + position * 12, fill='green')
            w.itemconfigure(97 + position, text="大")
            position += 1
        case "学":
            w.itemconfigure(1 + position * 12, fill='black')
            w.itemconfigure(4 + position * 12, fill='black')
            w.itemconfigure(5 + position * 12, fill='black')
            w.itemconfigure(6 + position * 12, fill='black')
            w.itemconfigure(7 + position * 12, fill='black')
            w.itemconfigure(8 + position * 12, fill='black')
            w.itemconfigure(11 + position * 12, fill='black')
            w.itemconfigure(12 + position * 12, fill='black')
            w2.itemconfigure(1 + position * 12, fill='green')
            w2.itemconfigure(4 + position * 12, fill='green')
            w2.itemconfigure(5 + position * 12, fill='green')
            w2.itemconfigure(6 + position * 12, fill='green')
            w2.itemconfigure(7 + position * 12, fill='green')
            w2.itemconfigure(8 + position * 12, fill='green')
            w2.itemconfigure(11 + position * 12, fill='green')
            w2.itemconfigure(12 + position * 12, fill='green')
            w.itemconfigure(97 + position, text="学")
            position += 1
        case "深":
            w.itemconfigure(1 + position * 12, fill='black')
            w.itemconfigure(6 + position * 12, fill='black')
            w.itemconfigure(8 + position * 12, fill='black')
            w.itemconfigure(10 + position * 12, fill='black')
            w.itemconfigure(11 + position * 12, fill='black')
            w.itemconfigure(12 + position * 12, fill='black')
            w2.itemconfigure(1 + position * 12, fill='green')
            w2.itemconfigure(6 + position * 12, fill='green')
            w2.itemconfigure(8 + position * 12, fill='green')
            w2.itemconfigure(10 + position * 12, fill='green')
            w2.itemconfigure(11 + position * 12, fill='green')
            w2.itemconfigure(12 + position * 12, fill='green')
            w.itemconfigure(97 + position, text="深")
            position += 1
        case "圳":
            w.itemconfigure(2 + position * 12, fill='black')
            w.itemconfigure(8 + position * 12, fill='black')
            w.itemconfigure(9 + position * 12, fill='black')
            w.itemconfigure(11 + position * 12, fill='black')
            w.itemconfigure(12 + position * 12, fill='black')
            w2.itemconfigure(2 + position * 12, fill='green')
            w2.itemconfigure(8 + position * 12, fill='green')
            w2.itemconfigure(9 + position * 12, fill='green')
            w2.itemconfigure(11 + position * 12, fill='green')
            w2.itemconfigure(12 + position * 12, fill='green')
            w.itemconfigure(97 + position, text="圳")
            position += 1
        case _:
            if(len(x) > 1):
                for i in range(len(x)):
                    judge(x[i])
            print(len(x))
def get_entry():
    x = entry.get()
    judge(x)
def clear():
    global position
    for i in range(1,97):
        w.itemconfigure(i, fill='white')
    for i in range(97, 105):
        w.itemconfigure(i, text="")
    for i in range(1, 97):
        w2.itemconfigure(i, outline="white", fill="red")
    entry.delete(0, END)
    position = 0

def generate_matrix(num, a, b):
    x1 = 0 + b
    y1 = 20 + b
    for i in range(3): # 18 lines 6 * 3
        x0 = 0 + a
        y0 = 20 + a
        x1 += 24
        y1 += 24
        for j in range(4):
            x0 += 24
            y0 += 24
            point = w.create_oval(x0, x1, y0, y1, fill="white", tags = num)
            num += 1
def generate_matrix2(num, a, b):
    x1 = 0 + b
    y1 = 20 + b
    for i in range(3): # 18 lines 6 * 3
        x0 = 0 + a
        y0 = 20 + a
        x1 += 24
        y1 += 24
        for j in range(4):
            x0 += 24
            y0 += 24
            point = w2.create_oval(x0, x1, y0, y1, fill="white", tags = num)
            num += 1

if __name__ == '__main__':
    window = Tk()
    window.title('Translator')
    frame = Frame(window, relief=SUNKEN, borderwidth=0, width=500, height=500)
    frame.pack(side=TOP, fill=BOTH, expand=1)
    w = Canvas(window, width=600, height=220)
    w2 = Canvas(window, width=600, height=240)
    w.place(x=0,y=0)
    w2.place(x=0, y=280)
    ft = tkinter.font.Font(family = '华文楷体',size=20)
    entry = Entry(window, bd = 2, font=ft)
    entry.place(x=125,y=215)
    b1 = Button(window, text = "Enter", command=get_entry)
    b1.place(x=210,y=260)
    b2 = Button(window, text = "Clear", command=clear)
    b2.place(x=260,y=260)

    generate_matrix(1, 20, 0)
    generate_matrix(13, 130, 0)
    generate_matrix(25, 240, 0)
    generate_matrix(37, 350, 0)
    generate_matrix(49, 20, 90)
    generate_matrix(61, 130, 90)
    generate_matrix(73, 240, 90)
    generate_matrix(85, 350, 90)
    w.create_text(90, 15, text="")
    w.create_text(200, 15, text="")
    w.create_text(310, 15, text="")
    w.create_text(420, 15, text="")
    w.create_text(90, 105, text="")
    w.create_text(200, 105, text="")
    w.create_text(310, 105, text="")
    w.create_text(420, 105, text="")

    generate_matrix2(1, 20, 0)
    generate_matrix2(13, 130, 0)
    generate_matrix2(25, 240, 0)
    generate_matrix2(37, 350, 0)
    generate_matrix2(49, 20, 90)
    generate_matrix2(61, 130, 90)
    generate_matrix2(73, 240, 90)
    generate_matrix2(85, 350, 90)
    for i in range(1, 97):
        w2.itemconfigure(i, outline="white", fill="red")
    w.create_text(250, 200, text="Braille Cells")
    w2.create_text(255, 200, text="Opening and closing positions of valves")

    window.mainloop()