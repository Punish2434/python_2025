# Chapter 5 - Dictionaries and Sets in Python

print("\n--- Dictionary Basics ---")
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Dictionary:", my_dict)
print("Name:", my_dict["name"])   # Access value
print("Age (using get):", my_dict.get("age"))

print("\n--- Add / Update / Delete ---")
my_dict["age"] = 26               # Update
my_dict["profession"] = "Engineer" # Add new key
print("After update:", my_dict)
del my_dict["city"]                # Delete key
print("After delete:", my_dict)

print("\n--- Dictionary Methods ---")
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
print("Check if 'name' in dict:", "name" in my_dict)

print("\n--- Nested Dictionary ---")
students = {
    "student1": {"name": "John", "age": 20},
    "student2": {"name": "Emma", "age": 22}
}
print("Nested dict:", students)
print("Student1 name:", students["student1"]["name"])

# ----------------------------- #
print("\n--- Set Basics ---")
my_set = {1, 2, 3, 4, 4, 5}  # Duplicates are removed
print("Set:", my_set)

print("\n--- Add / Remove Elements ---")
my_set.add(6)
print("After add:", my_set)
my_set.remove(3)
print("After remove:", my_set)

print("\n--- Set Operations ---")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)         # or set1.union(set2)
print("Intersection:", set1 & set2)  # or set1.intersection(set2)
print("Difference:", set1 - set2)    # Elements in set1 not in set2
print("Symmetric Difference:", set1 ^ set2)  # Elements in either but not both

print("\n--- Set Methods ---")
print("Length:", len(my_set))
print("Is 2 in set?", 2 in my_set)
my_set.clear()
print("After clear:", my_set)
