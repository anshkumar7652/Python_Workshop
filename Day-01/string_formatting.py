# python code for string formatting
y="Amit"
print("{:5}".format(10))
print("{:<5}".format(10))
print("{:15}".format(y))     #default string as left aligned
print("{:>15}".format(y))
print("{:^15}".format(y))

z2='Hello, '+ y
print(z2)
print('Hello, '+ y)

z3='Hello, {}' .format(y)
print(z3)
print('Hello, {}' .format(y))

z4='Hello, \n{}' .format(y)
print(z4)
print('Hello, \t{}' .format(y))

z5=f'Hello, {y}'
print(z5)
print(f'Hello, {y}')

#Unformatted Output
name = "Amit Keshav"
age = 25
print(name, age)

#formated
print("Name: %s Age: %d" % (name, age)) #%d %f %s %c
print("Name: {} Age: {}".format(name, age))
print(f"Name: {name} Age: {age}")

# python code for inputing a string and an integer value
print('Enter a Value: ',end='')
n1=input()
n2=input('Enter a Value: ')
n3=int(n2)
print("n3 is integer",n3)
print("Both values n1 and n2 are string",n1,n2,sep='...')
#sep is a string which is used in between different values of print()

