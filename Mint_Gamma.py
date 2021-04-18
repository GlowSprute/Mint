import random as rand #import randint
import sys
import os
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk
#-------------------------------------
def lvl():
    lvl1 = tk.Tk()
    lvl1.geometry("500x300")
    lvl1.resizable(0,0)
    lvl1.title("1 Уровень")
    txt = tk.Entry(lvl1, width=10)
    txt.place(x=1, y=100)
    txt.focus()
    lbl = tk.Label(lvl1, text="Загрузка...", font=("Arial Bold", 30))
    lbl.place(x=1, y=1)
    a=rand.randint(1,50)
    b=rand.randint(1,50)
    if a > b:
        r=rand.choice(('+','-'))
    else:
        r="+"
    if r =="+":
        lbl.configure(text=f"Сложи {a} и {b}")
        c = a + b
    elif r =="-":
        lbl.configure(text=f"Вычти {a} и {b}")
        c = a - b
    #------------------------
    def check():
        s = txt.get()
        if s.isnumeric():
            s=int(s)
            if c == s:      # Проверка
                messagebox.showinfo("Проверка:", "Молодец, верно!")
            else:
                messagebox.showinfo("Проверка:", "Неправильно!")
        lvl()
        lvl1.destroy()
    #-----------------------
    btn = tk.Button(lvl1, text="Проверить", command=check)
    btn.place(x=100, y=100)

def lvvl():
    lvl2 = tk.Tk()
    lvl2.geometry("500x300")
    lvl2.resizable(0,0)
    lvl2.title("2 Уровень")
    txt = tk.Entry(lvl2, width=10)
    txt.place(x=1, y=100)
    txt.focus()
    lbl = tk.Label(lvl2, text="Загрузка...", font=("Arial Bold", 30))
    lbl.place(x=1, y=1)
    a=rand.randint(1,500)
    b=rand.randint(1,500)
    if a > b:
        r=rand.choice(('+','-'))
    else:
        r="+"
    if r =="+":
        lbl.configure(text=f"Сложи {a} и {b}")
        c = a + b
    elif r =="-":
        lbl.configure(text=f"Вычти {a} и {b}")
        c = a - b
    #------------------------
    def check():
        s = txt.get()
        if s.isnumeric():
            s=int(s)
            if c == s:      # Проверка
                messagebox.showinfo("Проверка:", "Молодец, верно!")
            else:
                messagebox.showinfo("Проверка:", "Неправильно!")
        lvl()
        lvl2.destroy()
    #-----------------------
    btn = tk.Button(lvl2, text="Проверить", command=check)
    btn.place(x=100, y=100)
#-------------------------------------
win = tk.Tk()
win.geometry("900x500")
win.resizable(0,0)
win.title("Мята|Открытая Γамма")
win.resizable(False, False)
lbl = tk.Label(text="Здравствуйте, выберите уровень:", font=("Arial Bold", 30))
lbl.place(x=1, y=0)
btn = tk.Button(text="1 Уровень", font=("Arial Bold", 30), command=lvl)
btn.place(x=300, y=100)
btn1 = tk.Button(text="2 Уровень", font=("Arial Bold", 30), command=lvvl)
btn1.place(x=300, y=200)
btn2 = tk.Button()
tk.mainloop()


#(Это свободная программа: вы можете перераспространять ее и/или изменять
#   ее на условиях Стандартной общественной лицензии GNU в том виде, в каком
#   она была опубликована Фондом свободного программного обеспечения; либо
#   версии 3 лицензии, либо (по вашему выбору) любой более поздней версии.
#
#   Эта программа распространяется в надежде, что она будет полезной,
#   но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии ТОВАРНОГО ВИДА
#   или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной
#   общественной лицензии GNU.
#
#   Вы должны были получить копию Стандартной общественной лицензии GNU
#   вместе с этой программой. Если это не так, см.
#   <https://www.gnu.org/licenses/>.)