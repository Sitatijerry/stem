from tkinter import*
root = Tk()

def myClick():
    myLabel = Label(root, text = "Hey ! ")
    myLabel.pack()


myButton = Button(root, text ="click me", command = myClick, padx=10,pady=20,bg="grey",fg="yellow")
myButton.pack()

root.mainloop()