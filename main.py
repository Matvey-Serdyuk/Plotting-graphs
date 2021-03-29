import tkinter


from math import fabs


lencord = 20
width = "1020"
height = "580"


def proverka():
    global width, height, lencord
    width = (int(width) + lencord) - int(width) % (lencord + 20)
    height = int(height) + int(height) % ((lencord + 20) // 2)
    print(width, height, lencord)


def screen3_in_menu():
    global master2
    master2.destroy()
    screen1()


def screen2_in_menu():
    global master
    master.destroy()
    screen1()


def height_width():
    global entry1, width, height
    string = entry1.get()
    print(string)
    c = string.split("x")
    print(c)
    width = c[0]
    height = c[1]
    proverka()


def lencord_entry():
    global lencord, entry2
    string = entry2.get()
    print(string)
    lencord = int(string)
    proverka()

def printtext():
    global entry
    string = entry.get()
    print(string)
    f(string)


def f(primer):
    # ну блин в названии функции уже понятно что f(x)
    global lencord, width, height
    primer = primer[2:]
    print(primer)
    xy = []
    s = []
    for x in range(-4000, 4000):
        x /= 100
        for i in range(len(s)):
            if s[i] == "x":
                s[i] = str(x)
            primer = s.join("")
        y = eval(primer)
        xy.append(int(width) / 2 + x * lencord)
        xy.append(int(height) / 2 - y * lencord)
    canvas.create_line(xy, width="2.5")


def screen2():
    # графики
    global master1, lencord, width, height, master
    master1.destroy()
    master = tkinter.Tk()
    exit2 = tkinter.Button(master, text="меню", bg="yellow", command=screen2_in_menu)
    exit2.pack(anchor=tkinter.NE)
    global canvas
    canvas = tkinter.Canvas(master, width=width, height=height, bg="#999888")
    canvas.pack()
    # добавляет надпись X и Y
    canvas.create_text(int(width) / 2 - 12.5, 67.5, text="X", font="5")
    canvas.create_text(int(width) - 265, int(height) / 2 + 12.5, text="Y", font="5")
    # добавляет кординаты точек
    q = (int(width) - 520) // lencord // 2 * -1
    for i in range((int(width) - 520) // lencord):
        if q != 0:
            canvas.create_text(270 + i * lencord, int(height) / 2 - 12.5, text=str(q), font="2.5")
        q += 1
    q = (int(height) - 120) // lencord // 2
    for i in range((int(height) - 120) // lencord):
        if q != 0:
            canvas.create_text(int(width) / 2 + 14, 62.5 + lencord * i, text=str(q), font="2.5")
        q -= 1
    # ввод функции
    text = tkinter.Label(master, text="Введите уравнение прямой(например:y=x)")
    text.pack()
    global entry
    entry = tkinter.Entry(master, justify="center")
    entry.pack()
    entry.focus_set()
    but = tkinter.Button(master, text='ввести', command=printtext)
    but.pack()
    # создание кординатной сетки
    for i in range((int(height) - 20) // lencord + 1):
        k = 10 + i * lencord
        canvas.create_line(10, k, int(width) - 10, k, width="1")
    for i in range((int(width) - 20) // lencord + 1):
        k = 10 + i * lencord
        canvas.create_line(k, 10, k, int(height) - 10, width="1")
    # создание ox и oy
    canvas.create_line(260, int(height) / 2, int(width) - 260, int(height) / 2, width="2", arrow="last")
    canvas.create_line(int(width) // 2, 60, int(width) // 2, int(height) - 60, width="2", arrow="first")
    text3 = tkinter.Label(text="** это возвести в степень, * это умножить, / это делить, % это остаток, // это делить "
                               "нацело, fabs(x-1) это модуль x-1, +, -, = по стандарту")
    text3.pack()
    master.mainloop()


def screen1():
    # меню
    global master1
    master1 = tkinter.Tk()
    master1.geometry("1020x620")
    but1 = tkinter.Button(text="Начать построение графика", height=10, width=50, bg="#444555", command=screen2)
    but2 = tkinter.Button(text="Настройки", height=10, width=50, bg="#333555", command=screen3)
    but1.pack()
    but2.pack()
    master1.mainloop()


def screen3():
    # настройки
    global master1, entry1, master2, entry2, width, height, lencord, c
    master1.destroy()
    master2 = tkinter.Tk()
    master2.geometry("1020x620")
    but_in_menu = tkinter.Button(master2, command=screen3_in_menu, text="меню", bg="yellow")
    but_in_menu.pack()
    text1 = tkinter.Label(text="Настройки", font="5")
    text1.pack()
    entry1 = tkinter.Entry(master2, justify="center")
    entry1.pack()
    but_entry1 = tkinter.Button(master2, text="введите расширение экрана в px(например:1020x580, расширение не "
                                              "рекомендуется уменьшать)", command=height_width)
    entry2 = tkinter.Entry(master2, justify="center")
    but_entry2 = tkinter.Button(master2, text="введите длину 1 кординатного отрезка(Например: 20)", command=lencord_entry)
    text2 = tkinter.Label(text="Настройки работают не очень корректно")
    but_entry1.pack()
    entry2.pack()
    but_entry2.pack()
    text2.pack()
    master2.mainloop()


screen1()
