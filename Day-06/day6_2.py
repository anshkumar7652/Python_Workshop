# Declarative style using filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter (lambda x: x % 2 == 0, numbers))   #lamda checks for even no.s -> filter uses the lamda to add only the even to even_numbers list
print(even_numbers)
# Output: [2,4]