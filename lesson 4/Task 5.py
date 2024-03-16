from tkinter import*

root = Tk()
root.title("Calculator")
root.geometry("346x273")

e = Entry(root, width=55, bg = "white", fg = "black", borderwidth=5)
e.grid(row=0,column=0, columnspan=3)
e.insert(0, "")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    global f_num
    global math
    first_number = e.get()
    math = 'addition'
    f_num = float(first_number)
    e.delete(0, END)

def button_substract():
    global f_num
    global math
    first_number = e.get()
    math = 'substraction'
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    global f_num
    global math
    first_number = e.get()
    math = 'multiplication'
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    global f_num
    global math
    first_number = e.get()
    math = 'division'
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        result = f_num + float(second_number)
    elif math == 'substraction':
        result = 0,f_num - float(second_number)
    elif math == 'multiplication':
        result = f_num * float(second_number)
    elif math == 'division':
        result = f_num / float(second_number)

    e.insert(0, str(result))

def button_clear():
    e.delete(0, END)
a = 15
b = 2
c= 32

button1 = Button(root, text = "1", command=lambda: button_click(1), width=a, height=b)
button2 = Button(root, text = "2", command=lambda: button_click(2), width=a, height=b)
button3 = Button(root, text = "3", command=lambda: button_click(3), width=a, height=b)
button4 = Button(root, text = "4", command=lambda: button_click(4), width=a, height=b)
button5 = Button(root, text = "5", command=lambda: button_click(5), width=a, height=b)
button6 = Button(root, text = "6", command=lambda: button_click(6), width=a, height=b)
button7 = Button(root, text = "7", command=lambda: button_click(7), width=a, height=b)
button8 = Button(root, text = "8", command=lambda: button_click(8), width=a, height=b)
button9 = Button(root, text = "9", command=lambda: button_click(9), width=a, height=b)
button0 = Button(root, text = "0", command=lambda: button_click(0), width=a, height=b)
buttonClear = Button(root, text = "Clear", command=lambda: button_clear(), width=c, height=b)
buttonAdd = Button(root, text = "+", command=lambda: button_add(), width=a, height=b)
buttonSubstract = Button(root, text = "-", command=lambda: button_substract(), width=a, height=b)
buttonMultiply = Button(root, text = "*", command=lambda: button_multiply(), width=a, height=b)
buttonDivide = Button(root, text = "/", command=lambda: button_divide(), width=a, height=b)
buttonEqual = Button(root, text = "=", command=lambda: button_equal(), width=c, height=b)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=5, column=0)
buttonAdd.grid(row=6, column=0)
buttonSubstract.grid(row=7, column=0)
buttonMultiply.grid(row=7, column=1)
buttonDivide.grid(row=7, column=2)
buttonEqual.grid(row=6, column=1, columnspan=2)
buttonClear.grid(row=5, column=1, columnspan=2)


root.mainloop()
