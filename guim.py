from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import *
from  tkinter import messagebox


if(__name__== "__main__"):
    window = Tk()

    Scrollbar=Scrollbar(window)
    Scrollbar.pack(side=RIGHT,fill=Y)
    myList=Listbox(window,height=20,yscrollcommand=Scrollbar.set)

    myList.pack(side=LEFT,fill=BOTH)
    Scrollbar.config(command=myList.yview)

    window.mainloop()