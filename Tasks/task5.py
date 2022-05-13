#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Button, Label, Entry, Radiobutton, StringVar


"""
Напишите программу, в которой имеется несколько объединенных в группу радиокнопок, индикатор 
которых выключен (indicatoron=0). Если какая-нибудь кнопка включается, то в метке должна 
отображаться соответствующая ей информация. Обычных кнопок в окне быть не должно.
"""


def number1():
    label['text'] = '+4 961 572-13-56'


def number2():
    label['text'] = '+4 424 557-94-23'


def number3():
    label['text'] = '+4 234 777-77-77'


if __name__ == '__main__':
    root = Tk()
    root.title('Радиокнопки')
    root.geometry('250x200')

    var = StringVar()

    Radiobutton(indicatoron=0, text="Дмитрий", width=10, pady=5, command=number1, variable=var, value=0).pack()
    Radiobutton(indicatoron=0, text="Николай", width=10, pady=5, command=number2, variable=var, value=1).pack()
    Radiobutton(indicatoron=0, text="Игорь", width=10, pady=5, command=number3, variable=var, value=2).pack()
    label = Label(width=40, height=8)
    label.pack()

    root.mainloop()