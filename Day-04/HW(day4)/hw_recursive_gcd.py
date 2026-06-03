#Euclidean subtraction method to calc GCD  using recursion
def gcd(a, b):
    if a == b:
        return a      #base condition
    elif a < b:
        return(gcd(b,a))  #recursive call 1
    else:
        return(gcd(a-b,b))  #recursive call 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD =", gcd(a, b))