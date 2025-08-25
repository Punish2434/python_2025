# Chapter 5 - Practice Set Solutions

# Problem 1: Create a dictionary of Hindi words with English translation
print("\n--- Problem 1 ---")
dict_hindi = {
    "pustak": "book",
    "kutta": "dog",
    "billi": "cat",
    "pankha": "fan"
}
word = input("Enter a Hindi word (pustak/kutta/billi/pankha): ")
print("Meaning:", dict_hindi.get(word, "Word not found"))

# Problem 2: Input 8 numbers and display unique numbers
print("\n--- Problem 2 ---")
nums = []
for i in range(8):
    n = int(input(f"Enter number {i+1}: "))
    nums.append(n)
unique_nums = set(nums)
print("Unique numbers:", unique_nums)

# Problem 3: Can we have a set with 18(int) and '18'(str)?
print("\n--- Problem 3 ---")
s = {18, "18"}
print("Set with int and str:", s)

# Problem 4: Length of set after operations
print("\n--- Problem 4 ---")
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print("Set:", s)
print("Length:", len(s))  # length = 2 because 20 == 20.0

# Problem 5: Type of empty set
print("\n--- Problem 5 ---")
s = {}
print("Type of {} is:", type(s))   # dict
s = set()
print("Type of set() is:", type(s))  # set

# Problem 6: Empty dictionary, store 4 friends' favourite languages
print("\n--- Problem 6 ---")
fav_lang = {}
fav_lang["Shubham"] = input("Enter Shubham's favourite language: ")
fav_lang["Ankit"] = input("Enter Ankit's favourite language: ")
fav_lang["Sonali"] = input("Enter Sonali's favourite language: ")
fav_lang["Harshita"] = input("Enter Harshita's favourite language: ")
print("Favourite languages:", fav_lang)

# Problem 7: If names of 2 friends are same
print("\n--- Problem 7 ---")
print("If two keys (names) are same, the later value will overwrite the previous one.")

# Problem 8: If languages of 2 friends are same
print("\n--- Problem 8 ---")
print("If two values are same, it’s allowed. Dictionary only requires keys to be unique.")

# Problem 9: Can you change values inside a list within a set?
print("\n--- Problem 9 ---")
print("No, because lists are mutable and cannot be stored inside a set (TypeError).")
