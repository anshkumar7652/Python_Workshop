#String Indexing and Slicing

x = "Python"
print(x[0]) #indexing
print(x[1])

#variable[start : stop : step]
#Slicing
print(x[1:4])
print(x[:4])
print(x[2:])
print(x[0:6:2])
print(x[::-1]) #Reverse String
print(x[::1])
print(x[::])

# String slicing 
String ='STRING'
# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)
print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])