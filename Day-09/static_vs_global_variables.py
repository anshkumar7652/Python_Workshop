'''
class Student:
    global coll                                         #this statement has no use here
    college ='ABC College'   #static
    coll='ABC'
    def __init__(self,name):
        self.name=name  #instance
coll ='XYZ'  #global var
print(coll)
s1=Student('Rahul')
s2=Student('Priya')
print(s1.college)
print(s2.college)
Student.college='NIET'
print(s1.college)
print(s2.college)

'''
coll ='XYZ'  #global var   < --since globalvar is now initialized before the class the statement 'global coll' becomes useful
class Student:                                    
    global coll              #now this statement serves a purpose in changing 'XYZ' --> 'ABC'
    college ='ABC College'   #static
    coll='ABC'
    def __init__(self,name):
        self.name=name  #instance

print(coll)
s1=Student('Rahul')
s2=Student('Priya')
print(s1.college)
print(s2.college)
Student.college='NIET'
print(s1.college)
print(s2.college)