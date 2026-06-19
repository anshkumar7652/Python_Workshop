from tkinter import *

# Function FIRST
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator_entry.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Divide by zero"
        else:
            result = "Invalid operator"

        lbl_result.config(text="Result = " + str(result))

    except:
        lbl_result.config(text="Invalid input")


# Main Window
root = Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Inputs
Label(root, text="First Number").pack(pady=5)
entry1 = Entry(root)
entry1.pack()

Label(root, text="Second Number").pack(pady=5)
entry2 = Entry(root)
entry2.pack()

Label(root, text="Operator (+, -, *, /)").pack(pady=5)
operator_entry = Entry(root)
operator_entry.pack()

# Button
Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result Label
lbl_result = Label(root, text="Result = ")
lbl_result.pack()

root.mainloop()
