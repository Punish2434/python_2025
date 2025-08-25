# Chapter 11 - Inheritance and More on OOPs

# 1. Single Inheritance
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee.")

class Programmer(Employee):   # inherits from Employee
    def showLanguage(self):
        print("The default language is Python")


# 2. Multiple Inheritance
class Freelancer:
    company = "Upwork"
    level = 0

    def upgradeLevel(self):
        self.level += 1
        print("Level is now:", self.level)

class EmployeeBase:
    company = "Microsoft"

class HybridProgrammer(EmployeeBase, Freelancer):  # Multiple inheritance
    name = "Rohan"


# 3. Multilevel Inheritance
class Person:
    country = "India"

class Worker(Person):
    company = "Honda"

class Engineer(Worker):
    language = "Python"


# 4. super() keyword
class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()   # calls parent constructor
        print("Child Constructor")


# 5. Class Methods
class Manager:
    company = "Google"
    salary = 100

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal


# 6. Property Decorator
class EmployeeSalary:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value


# 7. Operator Overloading
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):   # operator overloading for +
        return self.num + other.num

    def __str__(self):   # string representation
        return f"Number: {self.num}"


# -------------------
# 🚀 TEST CASES
# -------------------

print("\n--- 1. Single Inheritance ---")
e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
p.showLanguage()

print("\n--- 2. Multiple Inheritance ---")
hp = HybridProgrammer()
print("Company:", hp.company)  # Microsoft (left-to-right order)
hp.upgradeLevel()
hp.upgradeLevel()

print("\n--- 3. Multilevel Inheritance ---")
eng = Engineer()
print("Country:", eng.country)
print("Company:", eng.company)
print("Language:", eng.language)

print("\n--- 4. super() Keyword ---")
c = Child()

print("\n--- 5. Class Method ---")
m = Manager()
print("Initial Salary:", m.salary)
m.changeSalary(500)
print("Updated Salary via object:", m.salary)
print("Updated Salary via class:", Manager.salary)

print("\n--- 6. Property Decorator ---")
emp = EmployeeSalary(4000)
print("Initial Salary:", emp.salary)   # calls getter
emp.salary = 6000                      # calls setter
print("Updated Salary:", emp.salary)

print("\n--- 7. Operator Overloading ---")
n1 = Number(10)
n2 = Number(15)
print("n1 + n2 =", n1 + n2)  # uses __add__
print("String representation:", n1)  # uses __str__
