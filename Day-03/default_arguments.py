#learing to use default arguments
def f_add(n1,n2=0):
    r=n1+n2
    return r
print(f_add(int(input('enter first number: ')),int(input('enter first number: '))))      #normal case
print(f_add(int(input('enter first number: '))))         #default case 