# Chapter 10 - OOP in Python

# 1. Class and Object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# 2. Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Person name: {self.name}")

class Teacher(Person):   # Inheriting Person
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

# 3. Polymorphism
class Bird:
    def sound(self):
        print("Some bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")

class Parrot(Bird):
    def sound(self):
        print("Squawk Squawk")

# 4. Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

# 5. Abstraction (using abc module)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# -------------------------------
# 🚀 TEST CASES
# -------------------------------
print("== Student Example ==")
s1 = Student("Harry", 85)
s1.display()

print("\n== Inheritance Example ==")
t1 = Teacher("Rahul", "Math")
t1.show()

print("\n== Polymorphism Example ==")
birds = [Sparrow(), Parrot(), Bird()]
for b in birds:
    b.sound()

print("\n== Encapsulation Example ==")
acc = BankAccount("Punish", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Final Balance:", acc.get_balance())

print("\n== Abstraction Example ==")
c = Circle(5)
print("Circle Area:", c.area())
