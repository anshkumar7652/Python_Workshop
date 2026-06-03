#checking whether the entered number is prime or not through functions
def inputval():   #definition keyword
    n=int(input('Enter number to check for prime: '))
    flag=isprime(n)
    display(flag,n)

def isprime(n):
    flag=True
    for i in range(2,n//2):
        if(n%i==0):
            flag= False
    return flag
    
def display(flag,n):
    if(flag):
        print(f'{n} is a prime number ')
    else:
        print(f'{n} is not a prime number ')

#main function
inputval()          