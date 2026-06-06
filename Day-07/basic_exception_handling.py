#exception handling
n1=10
n2=20
print(n1/n2)

#exception catching using try and except to avoid error 
n2=0
try:
    print(n1/n2)
except:
    print('division by zero is not defined')

#div by zero generates error if we dont use try and catch
n2=0
print(n1/n2)

#Exception                            Casuse
#ZeroDivisionError                    Division by zero
#ValueError                           Invalid value
#TypeError                            Wrong data type
#NameError                            Variable not defined
#IndexError                           Invalid list index
#KeyError                             Invalid dictionary key
#FileNotFoundError                    File does not exist
#AttributeError                       Invalid object attribute

try:
    n= int(input("Enter a number: "))
    print (100 / n)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid integer")










