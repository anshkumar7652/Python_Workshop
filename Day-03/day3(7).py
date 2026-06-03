#default arguements (continued)
def f_calc(n1, n2, n3 = 1 , n4 = 2 , n5 = 3 ):
    r2=n1-n2
    r1=n1+n2+n3+n4+n5 
    r3=n1*n5 
    if n2==0:
        r4 = n1 / n3
    
    else:
        r4 = n1 / n2
    return r1,r2,3,4
a,b,c,d = f_calc (1,2)
print(a,b,c,d,sep=":")
a,b,c,d = f_calc (5,0)
print(a,b,c,d,sep=":")
a,b,c,d = f_calc(1,2,3,4,5)
print(a,b,c,d,sep=":")