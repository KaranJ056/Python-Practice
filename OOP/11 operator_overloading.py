# operator overloading => ability of an operator to work as many forms

# means one operator is used to perform operations on multiple object types

# example:

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, obj):
        return ((self.m1+self.m2)+(obj.m1+obj.m2))
    
    def __gt__(self, obj):
        return ((self.m1+self.m2)>(obj.m1+obj.m2))

s1 = Student(45,66)
s2 = Student(76,79)

# it doen't work if we do not implement/overload the __add__() method in class
print(s1+s2)

if s1 > s2:
    print(f"s1 wins")
else:
    print(f"s2 wins")