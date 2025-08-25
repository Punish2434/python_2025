# Chapter 4 - Lists in Python

print("\n--- List Basics ---")
my_list = [1, 2, 3, "Hello", 4.5, True]
print("List:", my_list)

print("\n--- Indexing & Slicing ---")
fruits = ["apple", "banana", "cherry", "mango"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])
print("Slice [:2]:", fruits[:2])

print("\n--- List Methods ---")
nums = [10, 20, 30]
nums.append(40)
print("After append:", nums)
nums.insert(1, 15)
print("After insert:", nums)
nums.remove(20)
print("After remove:", nums)
nums.pop()
print("After pop:", nums)
nums.sort()
print("After sort:", nums)
nums.reverse()
print("After reverse:", nums)

print("\n--- Nested Lists ---")
nested = [[1, 2], [3, 4], [5, 6]]
print("Nested[1]:", nested[1])
print("Nested[1][0]:", nested[1][0])

print("\n--- List Comprehension ---")
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

print("\n--- Useful Functions ---")
nums = [3, 7, 2, 9]
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
