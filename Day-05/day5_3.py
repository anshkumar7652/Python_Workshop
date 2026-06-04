#learning closure functions in python
def outer():
    x=10
    def inner():
        print(x)
    return(inner)
f=outer()               #outer() finishes execution 
f()                     #inner() still remembers x
#the 'remembering' behaviour is what m,akes inner function closure,


