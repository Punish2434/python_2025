# Chapter 9 - File I/O

# 1. Write to a file (creates file if not exists)
with open("myfile.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("This is my first file I/O program.\n")

# 2. Append new data
with open("myfile.txt", "a") as f:
    f.write("Appending a new line.\n")

# 3. Read entire content
with open("myfile.txt", "r") as f:
    print("Full File Content:")
    print(f.read())

# 4. Read first 10 characters
with open("myfile.txt", "r") as f:
    print("\nFirst 10 chars:", f.read(10))

# 5. Read line by line
with open("myfile.txt", "r") as f:
    print("\nReading line by line:")
    for line in f:
        print(line, end="")

# 6. Using readline() and readlines()
with open("myfile.txt", "r") as f:
    print("\n\nUsing readline():", f.readline())
    f.seek(0)   # reset pointer
    print("Using readlines():", f.readlines())
