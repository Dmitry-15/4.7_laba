#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Button, Label, Entry, LEFT, END


"""
Перепишите предыдущую программу так, чтобы интерфейс выглядел по-другому.
"""


def red(event):
    ent1.delete(0, END)
    l1['text'] = "Красный"
    ent1.insert(0, "#ff0000")


def orange(event):
    ent1.delete(0, END)
    l1['text'] = 'Оранжевый'
    ent1.insert(0, "#ff7d00")


def yellow(event):
    ent1.delete(0, END)
    l1['text'] = 'Жёлтый'
    ent1.insert(0, "#ffff00")


def green(event):
    ent1.delete(0, END)
    l1['text'] = 'Зелёный'
    ent1.insert(0, "#00ff00")


def blue(event):
    ent1.delete(0, END)
    l1['text'] = 'Голубой'
    ent1.insert(0, "#007dff")


def dblue(event):
    ent1.delete(0, END)
    l1['text'] = 'Синий'
    ent1.insert(0, "#0000ff")


def purple(event):
    ent1.delete(0, END)
    l1['text'] = 'Фиолетовый'
    ent1.insert(0, "#7d00ff")


if __name__ == '__main__':
    root = Tk()
    root.title('Код цвета №2')
    root.geometry('350x150')

    l1 = Label(font="Arial 12", width=20)
    ent1 = Entry(width=20)
    but1 = Button(bg='#ff0000', width=5, height=2, pady=3)
    but2 = Button(bg='#ff7d00', width=5, height=2, pady=3)
    but3 = Button(bg='#ffff00', width=5, height=2, pady=3)
    but4 = Button(bg='#00ff00', width=5, height=2, pady=3)
    but5 = Button(bg='#007dff', width=5, height=2, pady=3)
    but6 = Button(bg='#0000ff', width=5, height=2, pady=3)
    but7 = Button(bg='#7d00ff', width=5, height=2, pady=3)

    but1.bind('<Button-1>', red)
    but2.bind('<Button-1>', orange)
    but3.bind('<Button-1>', yellow)
    but4.bind('<Button-1>', green)
    but5.bind('<Button-1>', blue)
    but6.bind('<Button-1>', dblue)
    but7.bind('<Button-1>', purple)

    l1.pack()
    ent1.pack()
    but1.pack(side=LEFT, padx=3, pady=3)
    but2.pack(side=LEFT, padx=3, pady=3)
    but3.pack(side=LEFT, padx=3, pady=3)
    but4.pack(side=LEFT, padx=3, pady=3)
    but5.pack(side=LEFT, padx=3, pady=3)
    but6.pack(side=LEFT, padx=3, pady=3)
    but7.pack(side=LEFT, padx=3, pady=3)

    root.mainloop()