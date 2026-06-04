# using generators
def numbers():
    return [1,2,3]
print (numbers())

#generators
def numbers():
    yield 1
    yield 2
    yield 3
g=numbers()
print(next(g))
print(next(g))
print(next(g))
#next() resumes execution until the next yield