class A:
    def speak(self):
        print('A speaks')
class D(A):
    
    def speak(self):
        super().speak()
        print('D speaks')
class C(A):
    def speak(self):
        print('C speaks')

A=A()
D=D()
C=C()

A.speak()
D.speak()
C.speak()
