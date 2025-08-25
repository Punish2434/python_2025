# Chapter 6 - Practice Set Solutions

# Problem 1: Greatest of four numbers entered by user
print("\n--- Problem 1 ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
greatest = max(a, b, c, d)
print("Greatest number is:", greatest)

# Problem 2: Pass or Fail (40% total + 33% in each subject)
print("\n--- Problem 2 ---")
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
total = (sub1 + sub2 + sub3) / 3

if total >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Pass")
else:
    print("Fail")

# Problem 3: Detect spam comments
print("\n--- Problem 3 ---")
text = input("Enter a comment: ")
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]
if any(keyword in text.lower() for keyword in spam_keywords):
    print("This is a spam comment.")
else:
    print("This is not spam.")

# Problem 4: Check username length
print("\n--- Problem 4 ---")
username = input("Enter a username: ")
if len(username) < 10:
    print("Username contains less than 10 characters.")
else:
    print("Username is valid.")

# Problem 5: Check if name is present in a list
print("\n--- Problem 5 ---")
names = ["Harry", "Rohan", "Shubham", "Sonali", "Divya"]
user_name = input("Enter a name: ")
if user_name in names:
    print(user_name, "is present in the list.")
else:
    print(user_name, "is not present in the list.")

# Problem 6: Student grade calculation
print("\n--- Problem 6 ---")
marks = int(input("Enter student marks: "))
if 90 <= marks <= 100:
    grade = "Ex"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

# Problem 7: Detect if post talks about "Harry"
print("\n--- Problem 7 ---")
post = input("Enter your post: ")
if "harry" in post.lower():
    print("Post is talking about Harry.")
else:
    print("Post is not talking about Harry.")
5