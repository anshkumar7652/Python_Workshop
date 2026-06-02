#Using f-strings (Best Modern Method)
x = 10


print(f"{x:5}") #default Number as R

#Left and Right Alignment
print(f"{10:<5}")
print(f"{10:>5}")

#Center Alignment
print(f"{10:^5}")

#Filling Empty Spaces
print(f"{10:*^6}")

#Example Table Formatting
print(f"{'Name': <10}{'Age':<5}")
print(f"{'Sandeep':<10}{25:<5}")

x1=111.9
print(f"{10:5}") #Width Formatting
print(f"{x1:15}") #Width Formatting

x2 = 133.14159
print(f"{x2:.2f}") #Decimal Precision
print(f"{x2:10.2f}")
print(f"x2 value = {x2:.2f}")
