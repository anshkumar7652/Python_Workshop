#format method and f-strings (continuation of day2(1).py)
n1=5
n2=10
res=n1+n2
print("Addition of {a} +{b}={c}".format(a=n1, b=n2, c=res))
print("Addition of {} + {} = {}".format(n1, n2, res))

#2.format() is a method of the string class (str)
#f-strings
print (f"Addition of {n1} + {n2} = {res}")

#older C-way
print("Addition of %d + %d = %d" %(n1, n2,res))


#constant string
print("{1} {0}".format("World", "Hello"))
print("{a} {b}".format(a="World", b="Hello"))
print("{b} {a}".format(a="World", b="Hello"))
