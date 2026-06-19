class Stud:
    def __init__(self, na, ag): # Local Variables. na, ag (constructor 1)
        self.name = na
        self.age = ag
    def __init__(self, na, ag): #Local Variables na, ag (constructor 2)
        self.name=na+'Kumar'
        self.age = ag + 2
    def input_v(self, n, a): #Local Variables n, a
        self.name = "Keshav"
        self.age = 30
    def display_v(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating an object
s1=Stud("Rahul", 20)
s1.display_v()
s1.input_v("Rahul", 20)
#Calling method
s1.display_v()


'''
##Python does not allows constructor overloading
incase of no user defined constructor -->  default constructor runs
incase of 2 user defined constructor -->  the last one becomes dominant and is run
incase of 1 user defined constructor  -->  the user  defined one dominates over the default constructor
'''