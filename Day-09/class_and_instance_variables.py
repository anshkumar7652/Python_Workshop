class abc2:
    n=10                                                                          #class variable
    def __init__(self,v1,v2):
        self.num1=v1                                                              #initializing instance variables
        self.num2=v2
    
    def f_add(self):
        print('Sum = ',self.num1+self.num2+abc2.n, "accessing num1-->",obj.num1)                                #adding instance and class variables

#main
n1=int(input('enter num 1: '))
n2=int(input('enter num2: '))
obj=abc2(n1,n2)
obj.f_add()
print(obj.num1)
print(abc2.n)
print(obj.n)                                                 
