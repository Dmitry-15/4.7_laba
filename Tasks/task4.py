#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Button, END, Text
from tkinter import filedialog as fd


"""
Напишите программу, состоящую из однострочного и многострочного текстовых полей и двух кнопок 
"Открыть" и "Сохранить". При клике на первую должен открываться на чтение файл, чье имя указано 
в поле класса Entry, а содержимое файла должно загружаться в поле типа Text. При клике на вторую 
кнопку текст, введенный пользователем в экземпляр Text, должен сохраняться в файле под именем, 
которое пользователь указал в однострочном текстовом поле.
"""


def opening():
    text.delete(1.0, END)
    open_file = fd.askopenfilename()
    with open(open_file, 'r', encoding="utf-8") as f:
        data = f.read()
    text.insert(1.0, data)


def saving():
    save_file = fd.asksaveasfilename(defaultextension=".txt", filetypes=(("Текстовый файл", "*.txt"),
                                                                         ("All files", "*.*"),))
    data = text.get(1.0, END)
    with open(save_file, 'w', encoding="utf-8") as f:
        f.write(data)


if __name__ == '__main__':
    root = Tk()
    root.title('Открытие и сохранение файла')
    root.geometry('650x700')

    text = Text(width=80, height=80)
    but1 = Button(text='Открыть', width=10, pady=6, command=opening)
    but2 = Button(text='Сохранить', width=10, pady=6, command=saving)

    but1.bind('<Button-1>', opening)
    but2.bind('<Button-1>', saving)

    but1.pack()
    but2.pack()
    text.pack()

    root.mainloop()