# Chapter 12 - Advanced Python I

from functools import reduce

# -----------------------------
# 1. Lambda Functions
# -----------------------------
square = lambda x: x * x
add = lambda a, b: a + b

print("\n--- 1. Lambda Functions ---")
print("Square of 5:", square(5))
print("Addition of 3 and 7:", add(3, 7))


# -----------------------------
# 2. Map, Filter, Reduce
# -----------------------------
nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
product = reduce(lambda x, y: x * y, nums)

print("\n--- 2. Map, Filter, Reduce ---")
print("Original list:", nums)
print("Squares:", squares)
print("Evens:", evens)
print("Product of all numbers:", product)


# -----------------------------
# 3. Enumerate
# -----------------------------
fruits = ["apple", "banana", "cherry"]

print("\n--- 3. Enumerate ---")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")


# -----------------------------
# 4. List Comprehension
# -----------------------------
squares_list = [x * x for x in nums]
evens_list = [x for x in nums if x % 2 == 0]

print("\n--- 4. List Comprehension ---")
print("Squares:", squares_list)
print("Evens:", evens_list)


# -----------------------------
# 5. Dictionary & Set Comprehension
# -----------------------------
squares_dict = {x: x * x for x in range(1, 6)}
unique_squares = {x * x for x in [1, 2, 2, 3, 4]}

print("\n--- 5. Dictionary & Set Comprehension ---")
print("Squares Dict:", squares_dict)
print("Unique Squares Set:", unique_squares)


# -----------------------------
# 6. *args and **kwargs
# -----------------------------
def demo_func(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)

print("\n--- 6. *args and **kwargs ---")
demo_func(1, 2, 3, name="Harry", age=25)


# -----------------------------
# 7. f-Strings
# -----------------------------
name = "Harry"
marks = 95
print("\n--- 7. f-Strings ---")
print(f"Hello, {name}. You scored {marks}% in Python.")


# Create sample files for Chapter 12 Problem 1

with open("1.txt", "w") as f:
    f.write("This is file 1. Hello from Python!\nLine 2 of file 1.\n")

with open("2.txt", "w") as f:
    f.write("This is file 2. Another example text.\nLine 2 of file 2.\n")

with open("3.txt", "w") as f:
    f.write("This is file 3. Last sample file for testing.\nLine 2 of file 3.\n")

print("✅ Sample files (1.txt, 2.txt, 3.txt) created successfully.")
