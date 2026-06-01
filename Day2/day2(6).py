#using for loop to print natural no of desired range
a=int(input('Enter starting number: '))    #taking input from user
b=int(input('Enter ending number: '))

if(a>b):
    for i in range(b,a+1):        #range(start,stop,increment)
        print(i)
else:
    for i in range(a,b+1):
        print(i)