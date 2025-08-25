# Chapter 10 - OOP Practice Set

# Problem 1: Programmer class
class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def info(self):
        print(f"Programmer {self.name} works on {self.product} at {self.company}")


# Problem 2: Calculator class
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def sqrt(self):
        return self.number ** 0.5

    @staticmethod
    def greet():
        print("Hello! Welcome to Calculator")


# Problem 3: Class attribute vs object attribute
class Sample:
    a = 5   # class attribute


# Problem 4: Train class
class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print(f"Train {self.name} has {self.seats} seats available")

    def fareInfo(self):
        print(f"Ticket price of {self.name} is Rs {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print("Ticket booked successfully!")
            self.seats -= 1
        else:
            print("Sorry, train is full!")


# Problem 5: Changing self parameter name
class Demo:
    def __init__(harry, value):  # instead of self, using 'harry'
        harry.value = value

    def show(harry):
        print("Value is:", harry.value)


# -------------------
# 🚀 TEST CASES
# -------------------
print("\n--- Problem 1 ---")
p1 = Programmer("Harry", "Skype")
p2 = Programmer("Rahul", "Teams")
p1.info()
p2.info()

print("\n--- Problem 2 ---")
Calculator.greet()
c = Calculator(9)
print("Square:", c.square())
print("Cube:", c.cube())
print("Square Root:", c.sqrt())

print("\n--- Problem 3 ---")
obj = Sample()
print("Class attribute Sample.a:", Sample.a)
print("Object attribute obj.a:", obj.a)
obj.a = 0   # changes only for this object
print("After setting obj.a = 0 → obj.a:", obj.a)
print("Class attribute still Sample.a:", Sample.a)

print("\n--- Problem 4 ---")
t = Train("Rajdhani Express", 2, 1500)
t.getStatus()
t.fareInfo()
t.bookTicket()
t.getStatus()
t.bookTicket()
t.bookTicket()

print("\n--- Problem 5 ---")
d = Demo(42)
d.show()
