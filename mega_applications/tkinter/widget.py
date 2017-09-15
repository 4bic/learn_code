from Tkinter import *

# create a window
window = Tk()

def km_to_miles():
    print("Success!")

# create widget button
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0, rowspan=2)

# entry panel
e1=Entry(window)
e1.grid(row=0, column=1)

# text field
t1 =Text(window,height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
