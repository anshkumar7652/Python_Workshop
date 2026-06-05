#imperative vs declarative programming
numbers=[1,2,3,4,5]
squares=[]
for n in numbers:
    squares.append(n**2)
print(squares)
#output : [1,4,5,16,25]


#declarative way
numbers=[1,2,3,4,5]
squares2=[n**2 for n in numbers]
print(squares2)
#outcome:[1,4,9,16,25]




