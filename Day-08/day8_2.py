#using user defined constructors and learning encapsulation

class Std:
    def __init__(self,r1=0,n1="",f1=0.0):
        self.rn=r1
        self.name=n1
        self.fee=f1
        
        
    def printval(self):
        print(self.rn,self.name,self.fee,sep='-')
        

#main
r=int(input('enter roll number: '))
f=float(input('enter fee: '))
n=input('enter name: ')

obj1=Std(r,n,f)
obj2=Std()
obj1.printval()
obj2.printval()