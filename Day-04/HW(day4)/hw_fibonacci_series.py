# Fibonacci Series Using Recursion

# Recursive function to find the nth Fibonacci number
def fibonacci(n):

    # Base condition 1
    if n == 0:
        return 0

    # Base condition 2
    elif n == 1:
        return 1

    # Recursive call
    return fibonacci(n - 1) + fibonacci(n - 2)


# Taking input from user
terms = int(input("Enter number of terms: "))

print("Fibonacci Series:")

# Printing Fibonacci series
for i in range(terms):
    print(fibonacci(i), end=" ")