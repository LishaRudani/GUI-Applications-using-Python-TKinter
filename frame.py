from tkinter import *
from tkinter import messagebox

if(__name__=="__main__"):
    window=Tk()
    window.title("My TK Window")
    window.geometry("300x200")

    f_lbl=Label(window,text="first label")
    s_lbl=Label(window,text="Second label")

    f_lbl.pack(side=LEFT)
    s_lbl.pack(side=RIGHT)

    f_lbl.grid(row=1,column=1)
    s_lbl.grid(row=2,column=2)

