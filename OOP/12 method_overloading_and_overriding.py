# Method Overloading
# Function with same name but different number of args or objs
# NOTE: Python doen't have this type of polymorphism
# means we can't do
# add(a,b)
# add(a,b,c)
# for this use case we have *args and **kwargs or we can use default args for that

# Method Overriding
# Function with same name but in different classess

# example:

class A:
    def show(self):
        print(f"Inside A's show")

class B(A):
    def show(self):
        print(f"Inside B's show")

b = B()

# if we don't have show() in B it will look in A and call A's show()
b.show()