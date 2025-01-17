# inheritance => extracting properties or behavior from parents
# in programming world getting properties from other class to your class is considered inheritance

# syntax:
# class Child_Class(Parent_Class):

# types of inheritance:
# 1. Single
# 2. Multiple
# 3. Multilevel
# 4. Hybrid

# Example:
class A:
    def feature1(self):
        print(f"Feature 1 working")

    def feature2(self):
        print(f"Feature 2 working")

class B(A):
    def feature3(self):
        print(f"Feature 3 working")

    def feature4(self):
        print(f"Feature 4 working")

class C(B):
    def feature5(self):
        print(f"Feature 5 working")

a1 = A()
b1 = B()
c1 = C()

# Because B is a child class of A we can see b1 can execute all methods of A
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

#  Because B is a child class of B which is child class of A we can see c1 can execute all methods of A and B
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

# ## NOTE: Pyhton resolves the issues and complexities of Muktiple Inheritance
#          using the MRO(Method Resolution Order) and C3 Linearization Algorithm