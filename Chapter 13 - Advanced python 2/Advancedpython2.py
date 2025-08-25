from functools import reduce

# 1. is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a == b:", a == b)   # True (same values)
print("a is b:", a is b)   # False (different objects)
print("a is c:", a is c)   # True (same object)

# 2. __name__ == "__main__"
if __name__ == "__main__":
    print("This script is running directly, not imported.")

# 3. Enumerate
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# 4. List comprehension
squares = [x*x for x in range(10) if x % 2 == 0]
print("Squares of even numbers:", squares)

# 5. Lambda function
cube = lambda x: x**3
print("Cube of 3:", cube(3))

# 6. Map, Filter, Reduce
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda x, y: x + y, nums)
print("Doubled:", doubled)
print("Even numbers:", even)
print("Sum:", sum_all)

# 7. Join and Split
sentence = "Python is fun"
words = sentence.split()
print("Split:", words)
joined = "-".join(words)
print("Joined with '-':", joined)
