#Keyword Arguments
def student(name, age):
    print(name, age)
student(age=20, name="Amit")

#Variable Length Arguments
def add(*args):
    print(sum(args))
add(10, 20)
add(10, 20, 30, 40)

#Variable-Length Keyword Arguments
def display(**kwargs):
    print(kwargs)
    print(f"c={kwargs['a']} and d={kwargs['b']}")
display(a="Amit", b=20)
display(a=1,b=2,c=3)
display(a=2.3,b=3.45)