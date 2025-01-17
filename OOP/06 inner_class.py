# inner class: class inside the class

# outer class
class Student:

    def __init__(self, name, rollno, brand, cpu, ram):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop(brand, cpu, ram)
    
    def show(self):
        print(f"{self.name} {self.rollno}")
        print(f"I have {self.lap.show()}")

    # inner class
    class Laptop:

        def __init__(self, brand, cpu, ram):
            self.brand = brand 
            self.cpu = cpu 
            self.ram = ram

        def show(self):
            return f"{self.brand} {self.cpu} {self.ram}gb"

# we can create inner class object inside outer class or 
# outside the outer class using outer class name

s1 = Student("Karan", 56, "hp", "i5", 8)
s2 = Student("Joshi", 45, "hp", "i5", 8)

s1.show()

lap1 = s1.lap
lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))

# lap1.show()