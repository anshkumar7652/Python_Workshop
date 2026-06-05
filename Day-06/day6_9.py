#learning tuple
t=(1,2,3,44,5,6 )
print(len(t))        #gives length of the tuple

print(max(t))        #gives the max element in the tuple

print(min(t))        #gives the min element in the tuple

print(sum(t))        #gives the sum of all elements in the tuple

print(t.index(44))   #gives the index of the element in the tuple       :  tuple_name.index(element)

print(t.count(3))    #gives the frequency of the element in the tuple   :  tuple_name.count(element)

print(sorted(t))     #sorts the tuple in ascending order and gives as a list

li=[1,2,3,7,4,6]
print(tuple(li))      #creates a tuple from entered sequence data type

t2=(1,2,3,'a',True,'b',2.5)
print(t2)