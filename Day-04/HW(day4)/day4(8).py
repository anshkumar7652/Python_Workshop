#Checking for prime number using recursion
def is_prime(n, i=2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)
n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime Number")
else:
    print("Not Prime Number")