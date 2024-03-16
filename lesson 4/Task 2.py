from tkinter import*

root = Tk()
root.geometry("300x250")
root.configure(bg = "orange")

Label1 = Label(root, text = "Hello world!", fg = "white", bg = "darkturquoise", borderwidth=20)
Label1.grid(row=0,column=0)
Label2 = Label(root, fg = "white", bg = "darkturquoise", borderwidth=20)
Label2.grid(row=0,column=5)
Label3 = Label(root, fg = "white", bg = "darkturquoise", borderwidth=20)
Label3.grid(row=1,column=0)
Label4 = Label(root, text = "My name is \n Andrey Shornikov!", fg = "white", bg = "darkturquoise", borderwidth=20)
Label4.grid(row=1,column=5)

root.mainloop()