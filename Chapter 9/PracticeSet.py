import os

# Q1: Write a program to read the file "poems.txt" and check whether it contains the word "twinkle".
with open("poems.txt", "r") as f:
    content = f.read()
    if "twinkle" in content:
        print("Q1: The word 'twinkle' is present in the file.")
    else:
        print("Q1: The word 'twinkle' is NOT present in the file.")


# Q2: Write a program to update a log file whenever Python runs.
with open("log.txt", "a") as f:
    f.write("Python run logged successfully!\n")
print("Q2: Log updated.")


# Q3: Write a program to read a log file and find whether it contains "python".
with open("log.txt", "r") as f:
    content = f.read().lower()
    if "python" in content:
        print("Q3: Found 'python' in log file.")
    else:
        print("Q3: 'python' not found in log file.")


# Q4: Write a program to find the line number where "python" is present.
with open("log.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        if "python" in line.lower():
            print(f"Q4: Found 'python' on line {i}")


# Q5: Write a program to make a new file and write some content into it.
with open("newfile.txt", "w") as f:
    f.write("This is a new file created for practice.\n")
print("Q5: newfile.txt created.")


# Q6: Write a program to replace "donkey" with "####" in a file.
with open("data.txt", "r") as f:
    content = f.read()

content = content.replace("donkey", "####")

with open("data.txt", "w") as f:
    f.write(content)
print("Q6: Replaced 'donkey' with '####' in data.txt.")


# Q7: Write a program to replace a list of words in a file.
words_to_replace = ["bad", "stupid", "ugly"]
with open("comments.txt", "r") as f:
    content = f.read()

for word in words_to_replace:
    content = content.replace(word, "####")

with open("comments.txt", "w") as f:
    f.write(content)
print("Q7: Replaced forbidden words in comments.txt.")


# Q8: Make a copy of a text file "this.txt".
with open("this.txt", "r") as f:
    content = f.read()
with open("copy_this.txt", "w") as f:
    f.write(content)
print("Q8: Copy created (copy_this.txt).")


# Q9: Find whether two files are identical.
def are_files_identical(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        return f1.read() == f2.read()

print("Q9:", "Files are identical." if are_files_identical("this.txt", "copy_this.txt") else "Files are different.")


# Q10: Wipe out the contents of a file.
open("temp.txt", "w").close()
print("Q10: Contents of temp.txt wiped out.")


# Q11: Rename a file to "renamed_by_python.txt".
if os.path.exists("temp.txt"):
    os.rename("temp.txt", "renamed_by_python.txt")
    print("Q11: File renamed to renamed_by_python.txt.")
else:
    print("Q11: File temp.txt does not exist to rename.")
