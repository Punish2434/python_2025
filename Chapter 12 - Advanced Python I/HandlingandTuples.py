# Chapter 12 - Exception Handling and Tuples

# -----------------------------
# 1. Exception Handling
# -----------------------------

print("\n--- Exception Handling ---")

# Basic try-except
try:
    x = int("10")
    print("Converted:", x)
except:
    print("❌ Error occurred while converting string to int.")

# Handling specific exceptions
try:
    a = 10
    b = 0
    print("Result:", a / b)
except ZeroDivisionError:
    print("❌ You cannot divide by zero!")
except ValueError:
    print("❌ Invalid input.")

# try-except-else
try:
    num = 5
    result = 10 / num
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
else:
    print("✅ No error, result is:", result)

# try-except-finally
try:
    f = open("nonexistent.txt")
except FileNotFoundError:
    print("❌ File not found.")
finally:
    print("This will always run (finally block).")

# Raising an exception manually
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print("Raised Exception:", e)


# -----------------------------
# 2. Tuples
# -----------------------------

print("\n--- Tuples ---")

# Creating tuples
t = (1, 2, 3, 4, 5)
print("Tuple:", t)
print("Type:", type(t))

# Accessing elements
print("First element:", t[0])
print("Last element:", t[-1])

# Tuple with single element
t1 = (1,)
print("Tuple with one element:", t1, "Type:", type(t1))

# Tuple methods
t2 = (1, 2, 3, 1, 4, 1)
print("Tuple:", t2)
print("Count of 1:", t2.count(1))
print("Index of 3:", t2.index(3))

# Tuple packing and unpacking
t3 = (10, 20, 30)
a, b, c = t3
print("Unpacked values:", a, b, c)
