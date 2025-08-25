# Chapter 11 - Practice Set (Inheritance & More on OOPs)

# -----------------------------
# Problem 1: Create C2dVector and C3dVector
# -----------------------------
class C2dVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"{self.i}i + {self.j}j"


class C3dVector(C2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


# -----------------------------
# Problem 2: Animals -> Pets -> Dog
# -----------------------------
class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    def bark(self):
        return "Woof! Woof!"


# -----------------------------
# Problem 3: Employee with Salary & Increment
# -----------------------------
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary - self.salary) / self.salary) * 100


# -----------------------------
# Problem 4: Complex Numbers with Operator Overloading
# -----------------------------
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# -----------------------------
# Problem 5: Vector in n dimensions
# -----------------------------
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __add__(self, other):
        return Vector([self.vec[i] + other.vec[i] for i in range(len(self.vec))])

    def __mul__(self, other):
        return sum([self.vec[i] * other.vec[i] for i in range(len(self.vec))])

    def __str__(self):
        return " + ".join(f"{self.vec[i]}e{i+1}" for i in range(len(self.vec)))

    def __len__(self):
        return len(self.vec)


# -----------------------------
# Problem 6: __str__ method to print nicely
# (already handled in Vector above)
# -----------------------------


# -----------------------------
# Problem 7: Override __len__ method (already done in Vector)
# -----------------------------


# -----------------------------
# Testing all problems
# -----------------------------
if __name__ == "__main__":
    # Problem 1 Test
    v2 = C2dVector(3, 4)
    v3 = C3dVector(1, 2, 3)
    print("2D Vector:", v2)
    print("3D Vector:", v3)

    # Problem 2 Test
    d = Dog()
    print("Dog Bark:", d.bark())

    # Problem 3 Test
    emp = Employee(10000, 10)
    print("Salary after increment:", emp.salaryAfterIncrement)
    emp.salaryAfterIncrement = 12000
    print("New increment %:", emp.increment)

    # Problem 4 Test
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    print("Complex Addition:", c1 + c2)
    print("Complex Multiplication:", c1 * c2)

    # Problem 5, 6, 7 Test
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print("Vector Sum:", v1 + v2)
    print("Dot Product:", v1 * v2)
    print("Vector Print (__str__):", v1)
    print("Vector Dimension (__len__):", len(v1))
