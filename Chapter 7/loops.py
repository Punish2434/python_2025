# Chapter 7 - Loops in Python

print("\n--- While Loop Example ---")
i = 1
while i <= 5:
    print("Hello Python", i)
    i += 1

print("\n--- For Loop Example ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n--- Range Example ---")
for i in range(1, 6):   # from 1 to 5
    print(i)

print("\n--- Break Example ---")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\n--- Continue Example ---")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n--- Else with Loop Example ---")
for i in range(5):
    print(i)
else:
    print("Loop finished successfully!")

print("\n--- Nested Loop Example ---")
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")
