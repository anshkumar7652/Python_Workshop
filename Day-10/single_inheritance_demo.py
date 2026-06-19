#inheritance in Python
class A:
    def f1(self):
        print('this is f1 of class A')


class B(A):
    def f2(self):
        print("This is f2 of class B")

#main
obj1=A()
obj1.f1()
obj2=B()
obj2.f2()
obj2.f1()


#obj1.f2        #gives error