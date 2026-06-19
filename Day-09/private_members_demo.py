# trying to access a private variable from outside the class 
class Stud:
    def __init__(self, n):            
        self.__name = n

    def f_display(self):
        print('STudent name: ',self.__name ,'<-- is a private variaBLE')
'''
def show(s):
    print("Student Name:", s.__name)

def display(m):
    print("Hello", m, s1.__name, sep="-")
'''
# Object Creation
s1 = Stud("Amit")

# Function Calls
s1.f_display()
#show(s1)
#print(s1.__name)