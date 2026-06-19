from tkinter import*
root=Tk()
var=IntVar()
Radiobutton(
    text='male',
    variable=var,
    value=1).pack()
Radiobutton(
    text='female',
    variable=var,
    value=2).pack()
root.mainloop()


