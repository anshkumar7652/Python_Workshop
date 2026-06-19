#c_test1 : Find the factorials of all prime numbers up to a given number n and print them as a list
class prg:
    def isprime(self,n):
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    
    def factorial(self,num):
        if num==0:
            return 1
        else:
            return self.factorial(num-1)*num
        
    def input(self,n):
        l=[]
        for i in range(2,n+1):
            if (self.isprime(i)==True):
                l.append(self.factorial(i))
        print(l)

obj=prg()
n=int(input("Enter number: "))
obj.input(n)