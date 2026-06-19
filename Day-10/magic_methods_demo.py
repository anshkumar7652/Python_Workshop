#using magic methods
n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))

result1=n1+n2
result2=n1.__add__(n2)
print(f"result1 = {result1}")
print(f"result1 = {result2}")