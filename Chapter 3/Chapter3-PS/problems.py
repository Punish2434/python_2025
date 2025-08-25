# Chapter 3 - Practice Set Solutions

# Problem 1: Display user entered name with Good Afternoon
print("\n--- Problem 1 ---")
name = input("Enter your name: ")
print("Good Afternoon,", name)

# Problem 2: Fill in a letter template with name and date
print("\n--- Problem 2 ---")
letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''
name = input("Enter your name: ")
date = input("Enter date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

# Problem 3: Detect double spaces in a string
print("\n--- Problem 3 ---")
st = "This is  a string with  double spaces."
index = st.find("  ")
print("Double spaces found at index:", index)

# Problem 4: Replace double spaces with single spaces
print("\n--- Problem 4 ---")
st = "This is  a string with  double  spaces."
st = st.replace("  ", " ")
print(st)

# Problem 5: Format a letter using escape sequence characters
print("\n--- Problem 5 ---")
letter = "Dear Harry,\n\tThis Python Course is nice.\nThanks!"
print(letter)
