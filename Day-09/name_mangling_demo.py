class Stud:
    def __init__(self,n):
        #NAME MANGLING
        self.__name=n     #it internally changes to --> self._Stud
s1 = Stud("Amit")
print(s1.__dict__)
#dict is a special attribute that stores all the instance
print(s1._Stud__name)
#The leading underscore is part of Python's name-mangling convention
