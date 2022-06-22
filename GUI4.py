from tkinter import *


def btnUp(e):
    global X, Y
    Y = Y - 5
    btn.place(x=X, y=Y)


def btnDown(e):
    global X, Y
    Y = Y + 5
    btn.place(x=X, y=Y)


X = 250
Y = 250
root = Tk()
root.geometry("500x500")
btn = Button(root, text="Submit", font=1)
btn.place(x=X, y=Y)
root.bind("<Up>", btnUp)
root.bind("<Down>", btnDown)

root.mainloop()
