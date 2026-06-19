from tkinter import *

def show():
    print("Python =", python_var.get())
    print("Java =", java_var.get())
    print("C++ =", cpp_var.get())

root = Tk()
python_var = IntVar()
java_var = IntVar()
cpp_var = IntVar()

Checkbutton(root, 
            text="Python", 
            variable=python_var).pack()
Checkbutton(root, 
            text="Java", 
            variable=java_var).pack()
Checkbutton(root, 
            text="C++", 
            variable=cpp_var).pack()

Button(root, 
       text="Submit", 
       command=show).pack()

root.mainloop()