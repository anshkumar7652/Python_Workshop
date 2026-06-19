class prg: 
    def f_factorial(self,num):
        
        if(num==0):
            return 1
        else:
            return (num*self.f_factorial(num-1))
    def f_fibonacci(self,n):
        f=self.f_factorial(n)
        print('factorialof the enetered num: ',f)
        print('fibonacci series upto ',f,' is:')
        a,b=0,1
        c=0
        for i in range(f):
            print(a,end=' ')
            c=a+b
            a,b=b,c

#main
n=int(input('enter number: '))
obj=prg()
obj.f_fibonacci(n)