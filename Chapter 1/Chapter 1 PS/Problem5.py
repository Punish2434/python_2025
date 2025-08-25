import os  # Import the OS module to interact with the operating system

# List all files and folders in the current directory
files = os.listdir('.')  

print("Files in current directory:")
for f in files:  # Loop through each item
    print(f)     # Print the item name
