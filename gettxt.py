from tkinter import *
root = Tk()

#create text field space
e = Entry(root,width=50,bg ="blue",fg = "red")
e.pack()
e.insert(20, "Enter your name")
#create a function
def myClick():
        hello = "Hello " + e.get()
        My_label =Label(root, text = hello )
        My_label.pack()


#create a frame
My_button = Button(root,text = "Enter your name", command = myClick, fg = "black", bg= "red")

#pack it-----shove it in window
My_button.pack()   

root.mainloop()