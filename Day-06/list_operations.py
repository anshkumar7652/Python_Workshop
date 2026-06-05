#using list
a=[1,2.5,'as']
print(a)

#updating a value in list using negative indexing
a[-1]=20
print(a)


#updating a value in list using positive indexing
a[1]=20
print(a)



##adding value in list:

#using append --> adds value in the last of the list
a.append(30)
print(a)

#using insert --> ads value at desired index 
a.insert(1,25)    #insert(index,value)
print(a)

#using extend --> can use to adds multiple values but at the last of the list
a.extend([90,91,92])
print(a)


#deleting values in a list:

#using pop function --> delete a single element at the given index
a.pop(1)
print(a)

#using slicing to delete multiple elements that are in sequence in the list by proving a range
del a[3:5]
print(a)

#using remove funtion to delete matching elements by providing a element to match
a.remove(20)
print(a)

#using clear function to delete all elements in the list
a.clear()
print(a)



#sorting list and accesing max or min from the given list

a=[20,50,60,70,10,90]
print(a)

#using sort function
a.sort()
print(a)

#using reverse function
a.reverse()
print(a)