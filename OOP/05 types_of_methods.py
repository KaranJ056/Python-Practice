# we have 3 types of methods in Python

# 1. Instance methods
#       1. Accesor Methods
#       2. Mutator Methods
# 2. Class methods
# 3. Static methods

# ## NOTE: here static and class methods are not same as in variables

# Let's see through an example

class Student:
    # class variable
    school = "XYZ"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance methods
    def average_marks(self):
        return ((self.m1+self.m2+self.m3)/3)
    
    # Accessor = Getter
    def get_m1(self):
        return self.m1

    # Mutator = Setter
    def set_m1(self, m1):
        self.m1 = m1

    # Class Methods
    @classmethod
    def get_school(cls):
        return cls.school
    
    # static methods used when we are not working with any extra class or instance variables and methods
    #static methods
    @staticmethod
    def info():
        print("This is a Student class containing student marks of 3 subjects")

s1 = Student(12,34,24)
s2 = Student(56,45,67)

print(s1.average_marks())
print(s2.average_marks())

print(s1.get_m1())
s1.m1 = 35
print(s1.get_m1())

print(Student.get_school())
print(s1.get_school())

s1.info()
Student.info()