#using dictionary
d={'name':['abc','def'],'marks':[10,20]}             #creating a dictionar of 2 elements using {key:value},  key-->immutable, value-->mutable or immutable
print(d['name'])#-->['abc','def']                    #accesing element of the dict --> gives complete list which is an elem,ent of the dictionary
print(d['name'][0])#-->abc                           #accesing a an element of the list which inturn is an element of the dictonary

d['exp']=[20,24]                                     #adding an element to the dictionary
print(d)

#d['name'][0]='fgh'                                   #replacing an element of list which is an element of the dictionary :  ['abc','def'] --> ['fgh','def']
print(d)

d['name']='fgh'                                      #replacing the complete list with another element                   :  ['abc','def'] --> 'fgh'
print(d)
d['name']=['abc','def']

print(d.keys())                                      #printing only dictionary keys 
print(d.items())                                     #printing items of dictionary keys along with values


#deleting elemets
del d['name'][0]

d.pop('name')
d.popitem()
d.clear()