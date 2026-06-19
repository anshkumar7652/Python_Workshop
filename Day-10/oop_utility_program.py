class prg:
    def oddeven(self,n):
        if n%2==0:
            return True
   
    def factorial(self,num):
        if(num==0):
            return 1
        else:
            return num*self.factorial(num-1)
        
    def prime(self,n):
        for i in range(2,n//2+1):
            if(n%i==0):
                return False
        return True
    
    def greatestof3(self,n1,n2,n3):
        if(n1>=n2 and n1>=n3):
            return n1
        elif(n2>=n1 and n2>=n3):
            return n2
        elif(n3>=n1 and n3>=n2):
            return n3
    
    def vowels(self,str):
        s={''}
        str=str.lower()
        for i in range(len(str)):
            if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
                s.add(str[i])
        s.remove('')
        return s

#main
obj=prg()
n=int(input('Enter number to check for prime, oddeven and finding factorial '))

if(obj.oddeven(n)):
    print('Number is even')
else:
    print('Number is odd')

print("factorial of number is ",obj.factorial(n))
print("Number is prime: ",obj.prime(n))

n1=int(input("enter num1: "))
n2=int(input("enter num2: "))
n3=int(input("enter num3: "))
print('Greates of the three num is: ',obj.greatestof3(n1,n2,n3))

str=input('Enter string: ')
print('vowels in string are: ',obj.vowels(str))