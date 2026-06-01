#using nested if else to implement logic
a=int(input('Enter first number: '))      #type casting to int since input() by default takes input as string
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
if(a>b):
    if(a>c):
        print("",a," is greatest")
    else:
        print("",c," is greatest")
else:
    if(b>c):
        print("",b," is greatest")
    else:
        print("",c," is greatest")
        