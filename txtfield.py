from tkinter import *
root = Tk()
#create a function
def myClick():
        My_label =Label(root, text = "Hey you clicked me!!")
        My_label.pack()


#create a frame
My_button = Button(root,text = "Click me", command = myClick, fg = "black", bg= "red")

#pack it-----shove it in window
My_button.pack()   

root.mainloop()