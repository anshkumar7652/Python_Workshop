#Write a Program to find roots of a quadratic expression.
import math
x2=int(input('enter coefficent of x^2: '))
x1=int(input('enter coefficent of x^1: '))
x0=int(input('enter coefficent of x^0: '))



if(x1*x1-(4*x2*x0)>=0):
    if(x1*x1-(4*x2*x0)==0):
        r1= (( -x1 ) + math.pow((x1*x1-(4*x2*x0)),0.5) ) / (2*x2)
        print('Roots of the equation [{}x^2 + {}x^1 + {}] are {} and {}'.format(x2,x1,x0,r1,r1))
    else:
        r1= (( -x1 ) + math.pow((x1*x1-(4*x2*x0)),0.5) ) / (2*x2)
        r2= (( -x1 ) - math.pow((x1*x1-(4*x2*x0)),0.5) ) / (2*x2)
        print('Roots of the equation [{}x^2 + {}x^1 + {}] are {} and {}'.format(x2,x1,x0,r1,r2))
else:
    print("Equation has complex roots")