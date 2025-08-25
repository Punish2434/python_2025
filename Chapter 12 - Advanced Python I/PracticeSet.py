# Chapter 12 - Practice Set (Exception Handling, Tuples, List Comprehension, File I/O)

# -------------------------
# Problem 1
# -------------------------
print("\nProblem 1: Open three files safely")
filenames = ["1.txt", "2.txt", "3.txt"]
for file in filenames:
    try:
        with open(file, "r") as f:
            print(f"Contents of {file}:")
            print(f.read())
    except FileNotFoundError:
        print(f"❌ {file} not found. Skipping without exiting program.")


# -------------------------
# Problem 2
# -------------------------
print("\nProblem 2: Print 3rd, 5th and 7th element from a list")
my_list = ["apple", "banana", "cherry", "date", "fig", "grape", "mango", "orange"]
print("Original List:", my_list)

for idx, item in enumerate(my_list, start=1):
    if idx in [3, 5, 7]:
        print(f"{idx}th element:", item)


# -------------------------
# Problem 3
# -------------------------
print("\nProblem 3: Multiplication table using list comprehension")
n = 5  # you can change this or use input: int(input("Enter a number: "))
table = [n * i for i in range(1, 11)]
print(f"Multiplication Table of {n}:", table)


# -------------------------
# Problem 4
# -------------------------
print("\nProblem 4: Division with ZeroDivision handling")
a, b = 10, 0   # you can also take input
try:
    result = a / b
except ZeroDivisionError:
    result = "Infinite (division by zero handled)"
print(f"{a}/{b} =", result)


# -------------------------
# Problem 5
# -------------------------
print("\nProblem 5: Save multiplication table into file")
n = 7
table = [n * i for i in range(1, 11)]

with open("Tables.txt", "w") as f:
    f.write(f"Multiplication Table of {n}:\n")
    for i, val in enumerate(table, start=1):
        f.write(f"{n} x {i} = {val}\n")

print("✅ Multiplication table saved in 'Tables.txt'")
