#learning match case
x=int(input('Enter a number: '))

match x:                          #learning match case for integer
    case 1:
        print('one')
    case 2:
        print('two')


x=input()
match x:                          #learning match case with string
    case 'python':
        print('mathed')
    case 'py':
        print('matched')

x=bool(input())
match x:                           #learning match case with boolean
    case True:
        print('matched')
    case False:
        print('matched')

x=int(input())
match x:                            #learning match case with multiple cases
    case 6 | 7:
        print("Weekend")
    case 1|2|3|4|5:
        print("Weekday")

x=input()
match x:                             #using always true case using an uninitialized variable
    case value:
        print("ALways true")

x=int(input())
match x:                             #using if condition in case statement
    case n if n>10:
        print("Greater than 10")
    case _:
        print("10 or less")