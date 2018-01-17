from tkinter import *
import tkinter
from functools import partial

def select(value):
    global upletter
    if value == " Space ":
        entry.insert(tkinter.END, ' ')
    elif value == "Tab":
        entry.insert(tkinter.END, '    ')
    elif value == "CapsLock":

        if upletter == 0:
            upletter = 1
        else:
            upletter = 0
    else:
        if upletter == 0:
            entry.insert(tkinter.END, value)
        else:
            entry.insert(tkinter.END, value.upper())

Keyboard_app = tkinter.Tk()
Keyboard_app.title("Onscreen Keyboard")
Keyboard_app ['bg'] = 'powder blue'
Keyboard_app.resizable(0, 0)
upletter = 0

label = Label(Keyboard_app, text="Onscreen Keyboard", font=('arial', 30, 'bold'), bg='powder blue', fg="#000000").grid(row=0, columnspan=40)
entry = Text(Keyboard_app, width=138, font=('arial', 10, 'bold'))
entry.grid(row=1, columnspan=40)

buttons = ['!', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-',
           'Tab', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
           'CapsLock', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', '"', '1', '2', '3', '/',
           ' Space ']

varRow = 3
varColumn = 0

for button in buttons:
    command = lambda x = button: select(x)
    if button != " Space ":
        tkinter.Button(Keyboard_app, text=button, width=7, padx=3, pady=3, bd=12, bg='powder blue',
                       font=('arial', 12, 'bold'), activebackground="#ffffff", activeforeground="#000990", relief='raised',
                       command=command).grid(row=varRow, column=varColumn)
    if button == " Space ":
        tkinter.Button(Keyboard_app, text=button, width=118, padx=3, pady=3, bd=12, bg='powder blue',
                       font=('arial', 12, 'bold'), activebackground="#ffffff", activeforeground="#000990", relief='raised',
                       command=command).grid(row=6, columnspan=16)

    varColumn += 1
    if varColumn > 15 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 15 and varRow == 4:
        varColumn = 0
        varRow += 1



Keyboard_app.mainloop()

