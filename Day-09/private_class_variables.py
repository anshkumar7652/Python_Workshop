class Stud:
    __col=23
    def __init__(self,r):
        self.rn=r
        print(self.__col)
s1=Stud(33)
print(s1)
print(Stud._Stud__col)
print(s1._Stud__col)