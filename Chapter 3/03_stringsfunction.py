txt = "  hello Python  "

print(len(txt))          # length → 15
print(txt.upper())       # HELLO PYTHON
print(txt.lower())       # hello python
print(txt.strip())       # removes spaces → "hello Python"
print(txt.replace("Python", "World"))  # hello World
print(txt.split())       # ['hello', 'Python']
print("Python" in txt)   # True
print("Java" not in txt) # True
