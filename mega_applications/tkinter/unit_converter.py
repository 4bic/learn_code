from Tkinter import *

# create a window
window = Tk()

def kg_to():
    # to grams
    grams =float(e1_value.get())*1000
    t1.insert(END, grams)
    # to pounds
    pounds =float(e1_value.get())*2.205
    t2.insert(END, pounds)
    # to ounces
    ounces =float(e1_value.get())*35.274
    t3.insert(END, ounces)

# create widget buttons
b1 = Button(window, text="convert from KG", command=kg_to)
b1.grid(row=0, column=0, rowspan=1)

# entry panel
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# labels
e1=Label(window,text="Grams")
e1.grid(row=3,column=0)

e1=Label(window,text="Pounds")
e1.grid(row=3,column=1)

e1=Label(window,text="Ounces")
e1.grid(row=3,column=2)

# text field
t1 =Text(window,height=1, width=10)
t1.grid(row=2, column=0)

t2 =Text(window,height=1, width=10)
t2.grid(row=2, column=1)

t3 =Text(window,height=1, width=10)
t3.grid(row=2, column=2)

window.mainloop()
