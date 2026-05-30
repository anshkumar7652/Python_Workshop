# python code for data types and memory size
import sys
# memory in bytes
a=10
b=5.5
c='A'
d='Amit'
z=2+3j
bol=True
print(sys.getsizeof(a))
print("a:", sys.getsizeof(a), "bytes")
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(z))
print(sys.getsizeof(bol))

#multiple assignment
m=n=p=5
print(m,n,p)
m1,m2,m3=2,3,4
print(m1,m2,m3)

#swapping without another variable
z1,z2=2,3
print(z1,z2)
z1,z2=z2,z1
print(z1,z2)
