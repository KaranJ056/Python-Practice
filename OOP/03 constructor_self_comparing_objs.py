class Computer():
    def __init__(self):
        self.name = "Karan"
        self.age = 20

    def updae_age(self):
        self.age = 30

    def __eq__(self, obj):
        return self.age == obj.age

    def compare(self, obj):
        return self.age == obj.age

comp1 = Computer()
comp2 = Computer()

comp1.name = "Joshi"

# By use of self keyword in method definitoion Python will decide which object we are referencing
comp1.updae_age()

print(f"{comp1.name} {comp1.age}")
print(f"{comp2.name} {comp2.age}")

# comparing two objects
# if comp1 == comp2:
#     print("They are of same age")
# we can't simply do as above because Python don't know how to compare two objects
# We can use Magic/Dunder methods for that

comp2.age = 30

# after implimenting __eq__ in calss definition we can do following
if comp1 == comp2:
    print("They are of same age") 
else:
    print("They are not of same age")

# or we can also use extra method for ex: compare(self, obj) to do the same
if comp1.compare(comp2):
    print("They are of same age") 
else:
    print("They are not of same age")