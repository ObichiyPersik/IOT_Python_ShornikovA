from tkinter import*

root = Tk()
root.geometry("400x200")
root.configure(bg = "orange")

e = Entry(root, width=50, bg = "blue", fg = "white", borderwidth=5)
e.pack(padx=0, pady=20)
e.insert(0, "Enter your name:")

def myClick():
    hello = "Hello " + e.get()
    Label1 = Label(root, text = hello)
    Label1.pack()

Button1 = Button(root, text = "Нажмите", command=myClick, bg = "white", fg = "blue", borderwidth=10)
Button1.pack(padx=6, pady=5)


root.mainloop()
