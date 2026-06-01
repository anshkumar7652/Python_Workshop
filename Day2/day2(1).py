#learning printing in different ways
a=5
b=10
s=a+b
print("Addition of",a,"+",b,"=",s)
print("Addition of {} + {} = {}".format(a,b,s))   ##.format() is a method of the string class (str)
print(f"Addition of {a} + {b} = {s}")



n1= int(input("Enter a number: "))
print("Enter another number: ",end='')
n2= input()
n2= int(n2)
result=n1+n2
#older C-way
print("Addition of %d + %d = %d" %(n1,n2,result))