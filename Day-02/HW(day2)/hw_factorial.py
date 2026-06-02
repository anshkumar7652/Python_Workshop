#Write a program to calculate factorial of a given number using for loop and while loop
a=int(input('enter number to find its factorial: '))
n=1
for i in range(1,a+1):
    n*=i
print(f'factorial of {a} is {n}')