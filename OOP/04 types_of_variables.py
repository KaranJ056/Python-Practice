# There are two types of variables for classes and objects in Python
# 1. Class Variables
# 2. Instance Variables

class Car:
    # Class Variable
    wheels = 4

    def __init__(self, name="BMW", mil=10):
        self.name = name
        self.mil = mil

car1 = Car()
car2 = Car()

print(f"{car1.name} has {car1.mil} milage and {car1.wheels} wheels")
print(f"{car2.name} has {car2.mil} milage and {car2.wheels} wheels")

# we can call/access class variables with direct class name
print(f"Every car has {Car.wheels} wheels")

# there are two namespace 
# 1. class namespcae => contains class variables and mathods
# 2. instance namespace => contains instance/object variables and mathods