from tkinter import *
root = Tk()
def myClick():
    MyLabel = Label(root,text= "Hey, you clicked")
    MyLabel.pack()
MyB = Button(root,text="click me!", command=myClick)
MyB.pack()
root.mainloop()