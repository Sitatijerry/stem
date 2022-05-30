from tkinter import *
root = Tk()
#create a frame
My_label1 = Label(root,text = "hello world")
My_label2 = Label(root,text = "hello world")
My_label3 = Label(root,text = "hello world")
#show it on screen
My_label1.grid(row=0,column=1)    
My_label2.grid(row=1,column=2)
My_label3.pack(row=2,column=3)
root.mainloop()