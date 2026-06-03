def fprint(v):    #v --> parameter
    print(v)

fprint('NIET')    #  NIET --> argument


# Function Without Arguments
def get_pi():
    return 3.14159
x = get_pi()
print(x)

# Function with default arguments
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Amit")