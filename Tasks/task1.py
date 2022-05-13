#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Button, Label, Entry


"""
Напишите простейший калькулятор, состоящий из двух текстовых полей, куда пользователь вводит числа, 
и четырех кнопок "+", "-", "*", "/". Результат вычисления должен отображаться в метке. Если 
арифметическое действие выполнить невозможно (например, если были введены буквы, а не числа), то 
в метке должно появляться слово "ошибка".
"""


def summa(event):
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        l1['text'] = num1+num2
    except ValueError:
        l1['text'] = 'Ошибка'


def subtraction(event):
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        l1['text'] = num1-num2
    except ValueError:
        l1['text'] = 'Ошибка'


def multiplication(event):
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        l1['text'] = num1*num2
    except ValueError:
        l1['text'] = 'Ошибка'


def division(event):
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        l1['text'] = num1/num2
    except ValueError:
        l1['text'] = 'Ошибка'


if __name__ == '__main__':
    root = Tk()
    root.title('Калькулятор')
    root.geometry('200x200')

    l1 = Label(font="Arial 14")
    ent1 = Entry(width=30)
    ent2 = Entry(width=30)
    but1 = Button(text='+')
    but2 = Button(text='-')
    but3 = Button(text='*')
    but4 = Button(text='/')

    but1.bind('<Button-1>', summa)
    but2.bind('<Button-1>', subtraction)
    but3.bind('<Button-1>', multiplication)
    but4.bind('<Button-1>', division)

    l1.config(bd=10)
    ent1.pack()
    ent2.pack()
    but1.pack()
    but2.pack()
    but3.pack()
    but4.pack()
    l1.pack()

    root.mainloop()
