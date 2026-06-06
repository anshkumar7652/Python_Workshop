#learning to read and modify files

# Reading complete file content at once
file = open("Day-07/a.txt", "r")      #Day-07/ ensures Python looks inside the Day-07 folder
content = file.read()
file.close()


# Writing (overwrites existing content)
with open("Day-07/a.txt", "w") as file:      #with statement automatically closes the file when done
    file.write("Hello, world!")              #"w" mode creates file if missing and overwrites existing content

# Appending (adds new content at the end)
with open("Day-07/a.txt", "a") as file:
    file.write("\nThis is a new line.")      #"a" mode preserves existing content and adds new data at the end


# Reading complete file after modifications
file = open("Day-07/a.txt", "r")
content = file.read()
print("reading complete file at once: ")
print(content)
file.close()                                #without "with" we have to explicitly close the file

print()

# Reading one line at a time
f = open("Day-07/a.txt", "r")
print("reading one line at a time: ")
print(f.readline()) #(Reads one line at a time)
print (f.readline())
print()
f.close()

# Reading all lines into a list
f= open("Day-07/a.txt", "r")
lines =f.readlines() #(Reads all lines and returns as list)
print (lines)
f.close()