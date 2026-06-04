numbers = [10, 20, 30]
for num in numbers:
    print(num)

#Internally
numbers = [10, 20, 30]
it = iter(numbers)
print (next(it))
print (next(it))
print (next(it))
print (next(it)) #StopIteration

#iter() converts an iterable into an iterator.
#next() retrieves the next value from an iterator.