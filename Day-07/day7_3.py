# Relative Backward Movement in binary mode
with open("Day-07/data.bin", "rb") as f:               #data.bin --> binary file
    f.seek(10)        # Move to byte position 10
    f.seek(-3, 1)     # Move back 3 bytes from current position (whence=1 means "from current")

    # General form: f.seek(offset, whence)
    # whence = 0 → from beginning (default)
    # whence = 1 → from current position
    # whence = 2 → from end of file

# Iterating Through a File (text mode)
with open("Day-07/a.txt", "r") as f:
    for line in f:
        print(line.strip())   # Print each line without extra newline


# Copying a File
with open("Day-07/a.txt", "r") as src:
    with open("Day-07/a2.txt", "w") as dest:
        dest.write(src.read())