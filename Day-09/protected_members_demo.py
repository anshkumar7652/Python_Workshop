'''class Stud:
    def __init__(self, n):            
        self.name = n

def show(s):
    print("Student Name:", s.name)

def display(m):
    print("Hello", m, s1.name, sep="-")

# Object Creation
s1 = Stud("Amit")

# Function Calls
display("Welcome")
show(s1)
print(s1.name)
'''
## Although protected still there is no difference between public and protected here  but if made private it can not be accessed
class Stud:
    def __init__(self, n):            
        self._name = n

def show(s):
    print("Student Name:", s._name)

def display(m):
    print("Hello", m, s1._name, sep="-")

# Object Creation
s1 = Stud("Amit")

# Function Calls
display("Welcome")
show(s1)
print(s1._name)

