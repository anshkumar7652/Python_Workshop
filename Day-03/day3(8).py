def f_sum(num1,*num):  #*num is used to take variable number of arguments
    result=num1
    for i in num:
        result+=i
    return result
r=f_sum(10,20,30)    #calling function with 3 arguments
print(f'then sum of numbers is: {r}')

r=f_sum(10,20,30,40,50)  #calling function with 5 arguments
print(f'then sum of numbers is: {r}')


