
from tkinter import *
windows =Tk()
windows.geometry("300x450")
windows.config()







expression_field = Entry(windows,width="26")


expression_field.grid(columnspan=4, ipadx=70)



button1 = Button(windows, text=' 1 ', fg='black', bg='red', height=3, width=7)
button1.grid(row=2, column=0, pady=30)

button2 = Button(windows, text=' 2 ', fg='black', bg='red', height=3, width=7)
button2.grid(row=2, column=1, pady=30)

button3 = Button(windows, text=' 3 ', fg='black', bg='red', height=3, width=7)
button3.grid(row=2, column=2, pady=30)

divide = Button(windows, text=' / ', fg='black', bg='red',  height=3, width=7)
divide.grid(row=2, column=3)

button4 = Button(windows, text=' 4 ', fg='black', bg='red', height=3, width=7)
button4.grid(row=3, column=0, pady=20)

button5 = Button(windows, text=' 5 ', fg='black', bg='red', height=3, width=7)
button5.grid(row=3, column=1, pady=20)

button6 = Button(windows, text=' 6 ', fg='black', bg='red', height=3, width=7)
button6.grid(row=3, column=2, pady=20)

plus = Button(windows, text=' + ', fg='black', bg='red',  height=3, width=7)
plus.grid(row=3, column=3)

button7 = Button(windows, text=' 7 ', fg='black', bg='red', height=3, width=7)
button7.grid(row=4, column=0, pady=20)

button8 = Button(windows, text=' 8 ', fg='black', bg='red', height=3, width=7)
button8.grid(row=4, column=1, pady=20)

button9 = Button(windows, text=' 9 ', fg='black', bg='red', height=3, width=7)
button9.grid(row=4, column=2)

minus = Button(windows, text=' - ', fg='black', bg='red',  height=3, width=7)
minus.grid(row=4, column=3)

multiply = Button(windows, text=' X ', fg='black', bg='red', height=3, width=7)
multiply.grid(row=5, column=0, pady=20)

zero = Button(windows, text=' 0 ', fg='black', bg='red', height=3, width=7)
zero.grid(row=5, column=1, pady=20)

dot = Button(windows, text=' . ', fg='black', bg='red', height=3, width=7)
dot.grid(row=5, column=2)

equal = Button(windows, text=' = ', fg='black', bg='red',  height=3, width=7)
equal.grid(row=5, column=3)


	# equal = Button(windows, text=' = ', fg='black', bg='red',
	# 			command=equalpress, height=1, width=7)
	# equal.grid(row=5, column=2)
    #
	# clear = Button(windows, text='Clear', fg='black', bg='red',
	# 			command=clear, height=1, width=7)
	# clear.grid(row=5, column='1')
    #
	# Decimal= Button(windows, text='.', fg='black', bg='red',
	# 				command=lambda: press('.'), height=1, width=7)
# Decimal.grid(row=6, column=0)
	# start the windows 
windows.mainloop()
