#learning recursion 

def d_input():
    n=int(input('enter number to calculate factorial: '))
    f=d_factorial(n)
    print(f'factorial of  {n} is {f}')

def d_factorial(n):                                     #recursive function to  calculate factorial of the entered number 
        
    if(n==0):
        return 1
    return n*d_factorial(n-1)                           #recursive call

 
#main
d_input()