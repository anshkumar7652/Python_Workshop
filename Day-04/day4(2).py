#learning about nested functions
def calculate(a, b):  #outer function
    def add():        #inner func(1)
        return a+b
    def multiply():   #inner func(2)
        return a*b
    print("Sum:", add())
    print("Product", multiply())
calculate (5, 3)
