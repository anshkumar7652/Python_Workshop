class A:
    def __init__(self):
        print("Parent constructor")

class B(A):
    def __init__(self):
        super().__init__()
        A.__init__(self)
        print("Child constructor")

obj1=A()
obj=B()   #although B has two constructors ,it by defaults runs its constructor by default
