from tkinter import *
from tkinter import messagebox

def addEmp():
    data=txtEid.get()

    data=txtSalary.get()

if(__name__=="__main__"):

    window=Tk()
    window.geometry("300x200")

    frame1=Frame(window)
    frame2=Frame(window)
    frame3=Frame(window)

    lblEid=Label(frame1,text="Id")
    lblname=Label(frame2,text="Name")
    lblsalary=Label(frame3,text="Salary")

    
    lblEid.grid(row=1)
    lblname.grid(row=2)
    lblsalary.grid(row=3)

    txtEid=Entry(frame1)
    txtName=Entry(frame2)
    txtSalary=Entry(frame3)

    txtEid.grid(row=1,column=2)
    txtName.grid(row=2,column=2)
    txtSalary.grid(row=3,column=2)
##########################################
    btnAdd=Button(frame2,text="Add",command=addEmp)
    btnSelect=Button(frame2,text="Select")
    btnDelete=Button(frame3,text="Delete")
    btnEdit=Button(frame3,text="Edit")

    
    
############################################
    Scrollbar=Scrollbar(frame3)
    Scrollbar.pack(side=RIGHT,fill=Y)
    myList=Listbox(frame3,height=5,yscrollcommand=Scrollbar.set)

    myList.pack(side=LEFT,fill=BOTH)
    Scrollbar.config(command=myList.yview)


    frame1.pack()
    frame2.pack()
    frame3.pack()

    window.mainloop()
    
    