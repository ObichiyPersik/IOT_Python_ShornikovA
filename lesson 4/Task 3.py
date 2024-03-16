from tkinter import*

root = Tk()
root.geometry("300x250")
root.configure(bg = "orange")

def myClick():
    Label1 = Label(root, text = "Нажата кнопка!", bg = "white", fg = "blue")
    Label1.pack()

Button1 = Button(root, text = "Нажмите", command=myClick, bg = "white", fg = "blue", borderwidth=10)
Button1.pack()

root.mainloop()
