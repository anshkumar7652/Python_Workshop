class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(self.name, self.roll, self.average())


def search_student(students, roll):
    for s in students:
        if s.roll == roll:
            return s
    return None


students = []

students.append(Student("Ansh", 1, [90, 80]))
students.append(Student("Rahul", 2, [70, 60]))
students.append(Student("Neha", 3, [50, 55]))

for s in students:
    s.display()

result = search_student(students, 2)

if result:
    result.display()
else:
    print("Not found")