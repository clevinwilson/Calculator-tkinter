
from tkinter import *
windows =Tk()
windows.geometry("350x530")
windows.config()

equation = StringVar()
expression = ""
screen = Entry(windows,width="35", textvariable=equation)#,font=('Helvetica',24)
screen.grid(columnspan=4, ipadx=70,pady=10)

clear_button = Button(windows, text=' Clr ', fg='white', bg='gray', command=lambda: clear(), height=3, width=7)
clear_button.grid(row=2, column=0, pady=10)

button1 = Button(windows, text=' 1 ', fg='white', bg='gray', command=lambda: press(1), height=3, width=7)
button1.grid(row=3, column=0, pady=30)

button2 = Button(windows, text=' 2 ', fg='white', bg='gray', command=lambda: press(2), height=3, width=7)
button2.grid(row=3, column=1, pady=30)

button3 = Button(windows, text=' 3 ', fg='white', bg='gray', command=lambda: press(3), height=3, width=7)
button3.grid(row=3, column=2, pady=30)

divide = Button(windows, text=' / ', fg='white', bg='gray', command=lambda: Operator("divide"),  height=3, width=7)
divide.grid(row=3, column=3)

button4 = Button(windows, text=' 4 ', fg='white', bg='gray', command=lambda: press(4), height=3, width=7)
button4.grid(row=4, column=0, pady=20)

button5 = Button(windows, text=' 5 ', fg='white', bg='gray', command=lambda: press(5), height=3, width=7)
button5.grid(row=4, column=1, pady=20)

button6 = Button(windows, text=' 6 ', fg='white', bg='gray', command=lambda: press(6), height=3, width=7)
button6.grid(row=4, column=2, pady=20)

plus = Button(windows, text=' + ', fg='white', bg='gray', command=lambda: Operator("plus"),  height=3, width=7)
plus.grid(row=4, column=3)

button7 = Button(windows, text=' 7 ', fg='white', bg='gray', command=lambda: press(7), height=3, width=7)
button7.grid(row=5, column=0, pady=20)

button8 = Button(windows, text=' 8 ', fg='white', bg='gray', command=lambda: press(8), height=3, width=7)
button8.grid(row=5, column=1, pady=20)

button9 = Button(windows, text=' 9 ', fg='white', bg='gray', command=lambda: press(9), height=3, width=7)
button9.grid(row=5, column=2)

minus = Button(windows, text=' - ', fg='white', bg='gray', command=lambda: Operator("minus"),  height=3, width=7)
minus.grid(row=5, column=3)

multiply = Button(windows, text=' X ', fg='white', bg='gray', command=lambda: Operator("multiply"), height=3, width=7)
multiply.grid(row=6, column=0, pady=20)

zero = Button(windows, text=' 0 ', fg='white', bg='gray', command=lambda: press(0), height=3, width=7)
zero.grid(row=6, column=1, pady=20)

dot = Button(windows, text=' . ', fg='white', bg='gray', command=lambda: press("dot"), height=3, width=7)
dot.grid(row=6, column=2)

equal = Button(windows, text=' = ', fg='white', bg='gray', command=lambda: equal(),  height=3, width=7)
equal.grid(row=6, column=3)

status=0
new_value=0
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)


def clear():
    global expression
    expression=" "
    equation.set(expression)

def Operator(Operator):
    global expression
    global olv
    global status
    if Operator == "plus":
        status = 1
        olv=expression
        expression = " "
        equation.set("+")
    elif Operator == "divide":
          status = 2
          olv=expression
          expression = " "
          equation.set("/")
    elif Operator == "minus":
          status = 3
          olv=expression
          expression = " "
          equation.set("-")
    else:
         status = 4
         olv = expression
         expression = " "
         equation.set("*")


def equal():
    if status == 1:
        new_value = expression
        result= int(new_value) + int(olv)
        equation.set(result)
    elif status == 2:
        new_value = expression
        result = int(olv) / int(new_value)
        equation.set(result)
    elif status == 3:
        new_value = expression
        result = int(olv) - int(new_value)
        equation.set(result)
    else:
        new_value = expression
        result = int(new_value) * int(olv)
        equation.set(result)


windows.mainloop()
