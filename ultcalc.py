from tkinter import *
root = Tk()

#create text field space
e1 = Entry(root,width=50,bg ="blue",fg = "red")
e1.pack()
e1.insert(0, "Enter first number ")
#second input
e2 = Entry(root,width=50,bg ="blue",fg = "red")
e2.pack()
e2.insert(0, "Enter second number ")



#create task function
def myClick():
       f_no = float(e1.get())
       s_no = float(e2.get())
       sub = f_no - s_no
       add = f_no + s_no
       div = f_no / s_no
       mult = f_no * s_no

       Ans = "Addition :" + str(add) + "\nsub:"+ str(sub) + "\ndiv:"+ str(div) +"\nmult:" +str(mult)
       My_label =Label(root, text = Ans )
       My_label.pack()


#create a frame
My_button = Button(root,text = "=", command = myClick, fg = "black", bg= "red")

#pack it-----shove it in window
My_button.pack()   

root.mainloop()