# Chapter 8 - Functions and Recursion

# 1. Simple Function (no parameter, no return)
def say_hello():
    print("Hello, Python!")

# Test
say_hello()


# 2. Function with Parameter
def greet(name):
    print(f"Good Afternoon, {name}")

# Test
greet("Harry")
greet("Rahul")


# 3. Function with Return Value
def add(a, b):
    return a + b

# Test
print("Addition:", add(5, 3))
print("Addition:", add(-2, 10))


# 4. Function with Default Arguments
def greet_default(name="Guest"):
    return f"Hello, {name}"

# Test
print(greet_default())
print(greet_default("Sohan"))


# 5. Function with Keyword Arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Test
student_info(age=20, name="Aman")


# 6. Function with Arbitrary Arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

# Test
print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))


# 7. Function with Arbitrary Keyword Arguments (**kwargs)
def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Test
print_details(Name="Rahul", Age=22, City="Delhi")


# 8. Recursive Function - Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))


# 9. Recursive Function - Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test
print("Fibonacci(5):", fibonacci(5))
print("Fibonacci(7):", fibonacci(7))


# 10. Recursive Function - Sum of first n numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

# Test
print("Sum of first 5 numbers:", sum_n(5))
print("Sum of first 10 numbers:", sum_n(10))
