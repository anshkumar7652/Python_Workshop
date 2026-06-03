#building calculator with basic functions
def f_calculation(a,b,op):
    match op:
        case '-':
            print(f' {a} - {b} = {a-b}')
        case '+':
            print(f' {a} + {b} = {a+b}')
        case '*':
            print(f' {a} * {b} = {a*b}')
        case '/':
            print(f' {a} / {b} = {a/b}')
        case _:
            print('invalid input')
            

a=int(input('Enter num1: '))
b=int(input('Enter num2: '))
op=input('choose operator: ')
f_calculation(a,b,op)