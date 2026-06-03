#list of tuples
students = [
     ("Amit", 85),
    ("Riya", 92),
    ("Sandeep", 78)
]

#Using Lambda with sorted()
students.sort(key=lambda x: x [1]) #Every tuple in list have x[]
print(students)
students.sort(key=lambda x: x[1], reverse=True)
print (students)

#Using Lambda with map()
numbers = [1, 2, 3, 4, 5]
squares =list (map(lambda x: x*x, numbers))
print (squares)

#Using Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]
evens =list (filter (lambda x: x % 2==0, numbers))

print (evens)

#Using Lambda with reduce ()
from functools import reduce
result = reduce (lambda a, b:a + b, [1, 2, 3, 4, 5])
#result reduce (lambda a, b: a *b, [1, 2, 3, 4, 5])
print(result)