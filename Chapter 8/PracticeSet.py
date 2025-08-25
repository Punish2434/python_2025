# Chapter 8 - Practice Set (Functions and Recursion)

# 1. Function to find greatest of three numbers
def greatest_of_three(a, b, c):
    return max(a, b, c)

print("Greatest of (5, 8, 3):", greatest_of_three(5, 8, 3))


# 2. Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))


# 3. Prevent print() from printing new line
print("Hello", end=" ")
print("World")   # Output: Hello World (in same line)


# 4. Recursive function to calculate sum of first n natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

print("Sum of first 5 natural numbers:", sum_natural(5))


# 5. Function to print first n lines of a pattern
def print_pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

print("Pattern for n=3:")
print_pattern(3)


# 6. Function to convert inches to cm
def inches_to_cm(inches):
    return inches * 2.54

print("10 inches in cm:", inches_to_cm(10))


# 7. Function to remove a given word from a list and strip spaces
def remove_word_from_list(lst, word):
    return [item.strip() for item in lst if item.strip() != word]
 
words = ["apple", "banana", " mango ", "banana", "grape "]
print("List after removing 'banana':", remove_word_from_list(words, "banana"))


# 8. Function to print multiplication table of a given number
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print("Multiplication Table of 7:")
multiplication_table(7)
