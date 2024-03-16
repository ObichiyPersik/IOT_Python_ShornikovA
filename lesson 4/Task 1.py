from tkinter import*

root = Tk()
root.geometry("300x250")
root.configure(bg = "orange")
Label1 = Label(root, text = "Hello world!", fg = "white", bg = "darkturquoise", borderwidth=20)
Label1.pack(padx = 6, pady = 70)

root.mainloop()