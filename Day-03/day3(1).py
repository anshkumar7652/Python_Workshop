#Using String Slicing to check for palindrome string
n1 = input("Enter a string: ")
if n1 == n1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")