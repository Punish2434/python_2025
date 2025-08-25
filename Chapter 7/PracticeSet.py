# Chapter 7 - Practice Set Solutions

# Problem 1: Multiplication table of a given number using for loop
print("\n--- Problem 1 ---")
n = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Problem 2: Greet all names in list starting with 'S'
print("\n--- Problem 2 ---")
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
for name in l1:
    if name.startswith("S"):
        print("Hello", name)

# Problem 3: Multiplication table using while loop
print("\n--- Problem 3 ---")
n = int(input("Enter a number for multiplication table (while loop): "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1

# Problem 4: Check if a number is prime
print("\n--- Problem 4 ---")
num = int(input("Enter a number to check prime: "))
prime = True
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
if prime and num > 1:
    print(num, "is Prime")
else:
    print(num, "is Not Prime")

# Problem 5: Sum of first n natural numbers using while loop
print("\n--- Problem 5 ---")
n = int(input("Enter n: "))
i, total = 1, 0
while i <= n:
    total += i
    i += 1
print("Sum of first", n, "natural numbers is:", total)

# Problem 6: Factorial of a given number using for loop
print("\n--- Problem 6 ---")
n = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is:", fact)

# Problem 7: Star pattern (increasing)
print("\n--- Problem 7 ---")
n = int(input("Enter n for star pattern: "))
for i in range(1, n+1):
    print("*" * i)

# Problem 8: Star pattern (decreasing)
print("\n--- Problem 8 ---")
n = int(input("Enter n for decreasing star pattern: "))
for i in range(n, 0, -1):
    print("*" * i)

# Problem 9: Star pattern (centered pyramid)
print("\n--- Problem 9 ---")
n = int(input("Enter n for pyramid star pattern: "))
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))

# Problem 10: Multiplication table in reverse order
print("\n--- Problem 10 ---")
n = int(input("Enter a number for reverse multiplication table: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n*i}")
