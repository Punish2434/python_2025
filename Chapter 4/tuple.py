# Chapter 5 - Tuples in Python

print("\n--- Creating Tuples ---")
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (1,)          # single element tuple must have a comma
t4 = tuple([4, 5]) # tuple from a list
print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("t4:", t4)

print("\n--- Indexing & Slicing ---")
fruits = ("apple", "banana", "cherry", "mango")
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

print("\n--- Tuple Methods ---")
a = (7, 0, 8, 0, 0, 9)
print("Tuple:", a)
print("Count of 0:", a.count(0))
print("Index of 8:", a.index(8))

print("\n--- Nested Tuples ---")
nested = (1, (2, 3), (4, 5))
print("nested[1]:", nested[1])
print("nested[1][0]:", nested[1][0])

print("\n--- Tuple Packing & Unpacking ---")
person = ("Alice", 25, "Engineer")
name, age, profession = person
print("Packed tuple:", person)
print("Unpacked:", name, age, profession)

print("\n--- Tuple Immutability ---")
tup = (10, 20, 30)
print("Original tuple:", tup)
try:
    tup[0] = 100  # This will raise an error
except TypeError as e:
    print("Error (tuples are immutable):", e)
