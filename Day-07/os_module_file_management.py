#exploring os commands
import os

# Get current directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# Checking File Existence
if os.path.exists("Day-07/a2.txt"):
    print("File exists")
else:
    print("File not found")

# Change directory
os.chdir(r"C:\ANSH(DRIVE-D)\Python_Workshop\Day-07")      #after changing directory, Python starts looking inside Day-07 by default

current_dir = os.getcwd()
print("Current Directory:", current_dir)

if os.path.exists("a2.txt"):
    print("File exists")
else:
    print("File not found")      #if a2.txt is not present in the current working directory