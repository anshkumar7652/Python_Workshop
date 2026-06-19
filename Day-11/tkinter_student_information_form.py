from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Student Information Form")
root.geometry("400x500")

# ---------------- Gender ----------------
Label(root, text="Select Gender", font=("Arial", 14, "bold")).pack(pady=10)

gender = StringVar(value="Male")

Radiobutton(root, text="Male", variable=gender, value="Male").pack()
Radiobutton(root, text="Female", variable=gender, value="Female").pack()

# ---------------- Skills ----------------
Label(root, text="Select Skills", font=("Arial", 14, "bold")).pack(pady=15)

python_skill = IntVar()
java_skill = IntVar()
cpp_skill = IntVar()

Checkbutton(root, text="Python", variable=python_skill).pack(anchor="center")
Checkbutton(root, text="Java", variable=java_skill).pack(anchor="center")
Checkbutton(root, text="C++", variable=cpp_skill).pack(anchor="center")

# ---------------- Hobbies ----------------
Label(root, text="Select Hobbies", font=("Arial", 14, "bold")).pack(pady=15)

hobby_list = Listbox(root, selectmode=MULTIPLE, height=4)
hobbies = ["Reading", "Music", "Sports", "Traveling"]

for hobby in hobbies:
    hobby_list.insert(END, hobby)

hobby_list.pack()

# ---------------- Course ----------------
Label(root, text="Select Course", font=("Arial", 14, "bold")).pack(pady=15)

course = ttk.Combobox(
    root,
    values=["Python", "Java", "C++", "Data Science", "Web Development"],
    state="readonly"
)
course.current(0)
course.pack()

# ---------------- Submit Function ----------------
def submit():
    skills = []

    if python_skill.get():
        skills.append("Python")
    if java_skill.get():
        skills.append("Java")
    if cpp_skill.get():
        skills.append("C++")

    selected_hobbies = [
        hobby_list.get(i)
        for i in hobby_list.curselection()
    ]

    info = f"""
Gender: {gender.get()}

Skills: {', '.join(skills)}

Hobbies: {', '.join(selected_hobbies)}

Course: {course.get()}
"""

    messagebox.showinfo("Student Information", info)

# ---------------- Submit Button ----------------
Button(root, text="Submit", command=submit).pack(pady=20)

root.mainloop()