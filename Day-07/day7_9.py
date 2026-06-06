#using parent class Exceptions to catch specific errors using inheritance concept off oops
try:
    n2= int(input("Enter a number: "))
    print (100 / n2)
except Exception as e:       #creating object e of parent class 'Exceptions'
    print("Caught exception: ",e)


try:
    n=int(input("Enter a number: "))
    result = 100 / n
except ZeroDivisionError:
    print("Division by zero")

except ValueError:
    print("Invalid input")
else:
    print("Result =", result)
finally:
    print("Thank you")


#user defined error
age = int(input("Enter age: "))
if age<18:
    raise ValueError("Age must be at least 18")
print("Eligible")


print("using raise:")

try:
    age = int(input("Enter age: "))
    if age<18:
        raise ValueError("Age must be at least 18")
    print("Eligible")
except ValueError as f:
    print("Error found: ",f)