#how to check closure
def outer():
    x=100
    #y=200
    def inner():
        return x #y
    return inner
f=outer()
print(f.__closure__)
print()
print(f.__closure__[0].cell_contents)
#print(f.__closure__[1].cell_contents)