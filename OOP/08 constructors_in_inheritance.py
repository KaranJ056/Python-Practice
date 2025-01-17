

class A:
    def __init__(self):
        print(f"Inside A")

    def feature1(self):
        print(f"Feature 1 working")

class B():
    def __init__(self):
        print(f"Inside B")

    def feature2(self):
        print(f"Feature 2 working")

class C(A, B):
    def __init__(self):
        super().__init__()
        print(f"Inside C")

    def feature3(self):
        print(f"Feature 3 working")

# NOTE: if sub class doesn't have any init method then and then it will go for Super class's init
#       To explicitly call suer class init we have to use super keyword
# MRO works left to right
c1 = C()