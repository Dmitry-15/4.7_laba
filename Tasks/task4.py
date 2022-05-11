#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


"""
Напишите программу, состоящую из однострочного и многострочного текстовых полей и двух кнопок 
"Открыть" и "Сохранить". При клике на первую должен открываться на чтение файл, чье имя указано 
в поле класса Entry, а содержимое файла должно загружаться в поле типа Text.
"""


def opening(event):
    text.delete(1.0, END)
    name = ent.get()
    with open(name, 'r', encoding="utf-8") as f:
        data = f.read()
    text.insert(1.0, data)


def saving(event):
    name = ent.get()
    data = text.get(1.0, END)
    with open(name, 'w', encoding="utf-8") as f:
        f.write(data)


if __name__ == '__main__':
    root = Tk()
    text = Text(width=80, height=20)
    ent = Entry(width=20)
    but1 = Button(text='Открыть', width=8, pady=5)
    but2 = Button(text='Сохранить', width=8, pady=5)
    but1.bind('<Button-1>', opening)
    but2.bind('<Button-1>', saving)
    ent.pack()
    but1.pack()
    but2.pack()
    text.pack()
    root.mainloop()