import os

# List all files in current directory
files = os.listdir('.')
print("Files in current directory:")
for f in files:
    print(f)
