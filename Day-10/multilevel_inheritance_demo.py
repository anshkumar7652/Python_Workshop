#inheritance(continued) in Python
class A:
    def f1(self):
        print('f1 of A')

class B(A):
    def f2(self):
        print('f2 of B')

class C(B):
    def f3(self):
        print('f3 of C')


#main
obj1=A()
obj2=B()
obj3=C()

obj1.f1()

obj2.f2()
obj2.f1()

obj3.f3()
obj3.f1()
obj3.f2()

