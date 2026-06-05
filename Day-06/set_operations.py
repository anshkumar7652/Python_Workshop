#sets  (same as in mathematics)

a={10,20,30}
print(a)

a.add(40)                                       #adds only one element at random position in the set 
print(a)

a.update([3,6,25,50])                           #adds multiple elements in the set at random positions
print(a)

a.remove(25)                                    #removes the element in the set if found else gives an error
print(a)

a.discard(60)                                   #removes the element in the set if found but DOES NOT gives an error if not found
print(a)

a.pop()
print("pop: ",a)

a.clear()                                       #removes all elements of the set
print(a)

a={1,2,3,4,5,6,7,8,9}
b={1,4,9,16,25}

c=a.union(b)                                    #gives union of the two sets
print(a,b,c)

d=a.intersection(b)                             #gives common elements of the two sets
print(d)

e=a.difference(b)                               #gives elements which are not common in both the sets
print(e)

m={1,2,3,4,5,6}
n={2,3,4}
print(m.issubset(n)) #--> false : m is not a subset of n
print(n.issubset(m)) #--> true  : n is a subset of m

print(m.issuperset(n)) #--> true : m is a superset of n
print(n.issuperset(m)) #--> false :n is not a superset of m

print(m.isdisjoint(n)) #-->false : the sets have common elements
print({1,2,3}.isdisjoint({4,5,6}))#-->true : the sets have no common elements 

