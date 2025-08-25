# Chapter 6 - Conditional Expressions in Python

print("\n--- Basic if Statement ---")
age = 18
if age >= 18:
    print("You are eligible to vote.")

print("\n--- if-else Statement ---")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("\n--- if-elif-else Ladder ---")
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

print("\n--- Nested if ---")
x = int(input("Enter a number: "))
if x > 0:
    if x % 2 == 0:
        print("Positive Even number")
    else:
        print("Positive Odd number")
else:
    print("Not a positive number")

print("\n--- One-line Conditional Expression (Ternary Operator) ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
min_value = a if a < b else b
print("Smaller number is:", min_value)

print("\n--- Logical Conditions ---")
age = int(input("Enter your age: "))
has_id = input("Do you have an ID card? (yes/no): ").lower()

if age >= 18 and has_id == "yes":
    print("Allowed to enter")
else:
    print("Not allowed")
