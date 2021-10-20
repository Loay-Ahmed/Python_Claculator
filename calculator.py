#! python3

############# importing Tkinter #############

from io import UnsupportedOperation
from tkinter import *
from tkinter.ttk import *

############# Defining Functions : clear , add , subtract , mult , dividion , ans , dot #############

def clear():
    entry.delete(0, END)

def number(n):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(n))

def ans():
    current = str(entry.get())
    entry.delete(0, END)
    answer = eval(current)
    entry.insert(0, str(answer))

def point():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + ".")

############# Creating and customizing main window #############

window = Tk()
window.title("Calculator")
window.geometry("300x245")
window.minsize(width=300, height=245)

############# Adding & Customizing Entry #############

entry = Entry(window)
entry.configure(width=36)
entry.grid(row=0, column=0, columnspan=3)

############# Adding & Customizing Buttons #############

ac = Button(window, text="AC", command=clear)
btn1 = Button(window, text="1", command=lambda:number(1))
btn2 = Button(window, text="2", command=lambda:number(2))
btn3 = Button(window, text="3", command=lambda:number(3))
btn4 = Button(window, text="4", command=lambda:number(4))
btn5 = Button(window, text="5", command=lambda:number(5))
btn6 = Button(window, text="6", command=lambda:number(6))
btn7 = Button(window, text="7", command=lambda:number(7))
btn8 = Button(window, text="8", command=lambda:number(8))
btn9 = Button(window, text="9", command=lambda:number(9))
btn0 = Button(window, text="0", command=lambda:number(0))
addi = Button(window, text="+", command=lambda:number("+"))
subtr = Button(window, text="-", command=lambda:number("-"))
mult = Button(window, text="*", command=lambda:number("*"))
divide = Button(window, text="/", command=lambda:number("/"))
equal = Button(window, text="=", command=ans)
dot = Button(window, text=".", command=point)

############# Placing Buttons #############

btn1.grid(row=3, column=0, ipady=15)
btn2.grid(row=3, column=1, ipady=15)
btn3.grid(row=3, column=2, ipady=15)
btn4.grid(row=2, column=0, ipady=15)
btn5.grid(row=2, column=1, ipady=15)
btn6.grid(row=2, column=2, ipady=15)
btn7.grid(row=1, column=0, ipady=15)
btn8.grid(row=1, column=1, ipady=15)
btn9.grid(row=1, column=2, ipady=15)
btn0.grid(row=4, column=0, columnspan=1, ipady=15)
addi.grid(row=1 , column=3, ipady=15)
subtr.grid(row=2, column=3, ipady=15)
mult.grid(row=3, column=3, ipady=15)
divide.grid(row=4, column=3, ipady=15)
equal.grid(row=4, column=2, ipady=15)
dot.grid(row=4, column=1, ipady=15)
ac.grid(row=0, column=3)

############# Running the App #############

window.mainloop()

