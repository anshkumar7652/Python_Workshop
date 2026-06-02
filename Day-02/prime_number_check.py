#wap in python to check whether the given number is prime or not
n=int(input("Enter a number: "))    #taking input from user
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")