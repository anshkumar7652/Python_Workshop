#binary files
with open("Day-07/data.bin", "wb") as f:
    f.write(b"Python")

with open("Day-07/data.bin", "rb") as f:
    print(f.read())

#Checking File Existence
import os

if os.path.exists("Day-07/a2.txt"):
    print("File exists")
else:
    print("File does not exists")