# Chapter 4 - Practice Set Solutions

# Problem 1: Store seven fruits in a list entered by the user
print("\n--- Problem 1: Seven Fruits ---")
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
print("Fruits List:", fruits)

# Problem 2: Accept names of 6 students and display them in a sorted manner
print("\n--- Problem 2: Sorted Student Names ---")
students = []
for i in range(6):
    name = input(f"Enter student {i+1} name: ")
    students.append(name)
students.sort()
print("Sorted Student Names:", students)

# Problem 3: Check that a tuple cannot be changed
print("\n--- Problem 3: Tuple immutability ---")
tup = (1, 2, 3)
print("Original tuple:", tup)
try:
    tup[0] = 100  # This will raise an error
except TypeError as e:
    print("Error:", e)

# Problem 4: Sum a list with 4 numbers
print("\n--- Problem 4: Sum of List ---")
nums = []
for i in range(4):
    n = int(input(f"Enter number {i+1}: "))
    nums.append(n)
print("Numbers:", nums)
print("Sum =", sum(nums))

# Problem 5: Count number of zeros in a tuple
print("\n--- Problem 5: Count Zeros in Tuple ---")
a = (7, 0, 8, 0, 0, 9)
print("Tuple:", a)
print("Number of zeros:", a.count(0))
