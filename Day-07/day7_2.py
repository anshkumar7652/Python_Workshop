# Using 'with' ensures the file closes automatically

# Reading from the file
with open("Day-07/a.txt", "r") as f:
    data = f.read()
    print(data)

# Writing to the file (overwrites content)
with open("Day-07/a.txt", "w") as f:
    f.write("Hello Python")
    f.flush()  # optional: forces immediate write