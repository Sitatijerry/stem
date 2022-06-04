import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""

def btn1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_add_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_sub_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def result():
    global A
    global operator
    global val
    A = int(val)
    operator = "="
    val = val + "="
    data.set(val)

def C_pressed():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
       x = int((val2.split("+")[1]))
       c = A + x
       data.set(c)
       val = str(c)
    elif operator == "-":
       x = int((val2.split("-")[1]))
       c = A - x
       data.set(c)
       val = str(c) 
    elif operator == "*":
       x = int((val2.split("*")[1]))
       c = A * x
       data.set(c)
       val = str(c)   
    elif operator == "/":
       x = int((val2.split("/")[1]))
    if x==0:
           messagebox.show("Error","Division by 0 not allowed")
           A==""
           val=""
           data.set(val)
    else:
            c=(A/x)
            data.set(c)
            val = str(c)


root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Sensei-calc")

data = StringVar()
lbl=Label(root,text="Label",anchor=SE,font=("Verdana",20),textvariable = data,bg="blue",fg="black",)
lbl.pack(expand=True,fill="both")

btnrow1=Frame(root,bg="black")
btnrow1.pack(expand=True,fill="both")

btnrow2=Frame(root,bg="black")
btnrow2.pack(expand=True,fill="both")

btnrow3=Frame(root,bg="black")
btnrow3.pack(expand=True,fill="both")

btnrow4=Frame(root,bg="black")
btnrow4.pack(expand=True,fill="both")

# button row 1
btn1 = Button(btnrow1,text = "1",font = ("Veranda",22),relief = GROOVE,border=0,command=btn1_isclicked,)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(btnrow1,text = "2",font = ("Veranda",22),relief = GROOVE,border=0,command=btn2_isclicked,)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(btnrow1,text = "3",font = ("Veranda",22),relief = GROOVE,border=0,command=btn3_isclicked,)
btn3.pack(side=LEFT,expand=True,fill="both")

# button add
btnadd = Button(btnrow3,text = "+",font = ("Veranda",22),relief = GROOVE,border=0,command=btn_add_clicked,)
btnadd.pack(side=LEFT,expand=True,fill="both")


# button row 2
btn4 = Button(btnrow2,text = "4",font = ("Veranda",22),relief = GROOVE,border=0,command=btn4_isclicked,)
btn4.pack(side=LEFT,expand=True,fill="both")

btn5 = Button(btnrow2,text = "5",font = ("Veranda",22),relief = GROOVE,border=0,command=btn5_isclicked,)
btn5.pack(side=LEFT,expand=True,fill="both")

btn6 = Button(btnrow2,text = "6",font = ("Veranda",22),relief = GROOVE,border=0,command=btn6_isclicked,)
btn6.pack(side=LEFT,expand=True,fill="both")

# button sub
btnsub = Button(btnrow3,text = "-",font = ("Veranda",22),relief = GROOVE,border=0,command=btn_sub_clicked,)
btnsub.pack(side=LEFT,expand=True,fill="both")


# button row 3
btn7 = Button(btnrow3,text = "7",font = ("Veranda",22),relief = GROOVE,border=0,command=btn7_isclicked,)
btn7.pack(side=LEFT,expand=True,fill="both")

btn8 = Button(btnrow3,text = "8",font = ("Veranda",22),relief = GROOVE,border=0,command=btn8_isclicked,)
btn8.pack(side=LEFT,expand=True,fill="both")

btn9 = Button(btnrow3,text = "9",font = ("Veranda",22),relief = GROOVE,border=0,command=btn9_isclicked,)
btn9.pack(side=LEFT,expand=True,fill="both")

# button mult
btnmul = Button(btnrow3,text = "*",font = ("Veranda",22),relief = GROOVE,border=0,command=btn_mul_clicked,)
btnmul.pack(side=LEFT,expand=True,fill="both")

# button row 4
btnC = Button(btnrow3,text = "C",font = ("Veranda",22),relief = GROOVE,border=0,command=C_pressed,)
btnC.pack(side=LEFT,expand=True,fill="both")

btn0 = Button(btnrow3,text = "0",font = ("Veranda",22),relief = GROOVE,border=0,command=btn0_isclicked,)
btn0.pack(side=LEFT,expand=True,fill="both")

btnequal = Button(btnrow3,text = "=",font = ("Veranda",22),relief = GROOVE,border=0,command=result,)
btnequal.pack(side=LEFT,expand=True,fill="both")

btndiv = Button(btnrow3,text = "/",font = ("Veranda",22),relief = GROOVE,border=0,command=btn_div_clicked,)
btndiv.pack(side=LEFT,expand=True,fill="both")

root.mainloop()