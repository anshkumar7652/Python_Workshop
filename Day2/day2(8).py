#cal gcd using while loop
n=int(input())
m=int(input())
while n!=m:
    if n>m:
        n=n-m
    else:
        n,m=m,n
print(f"GCD is {m}")