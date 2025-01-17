# class => blueprint
# object => actual thing/instance of that design

# Example:

class Computer:
    # Attributes => variables
    # Methods => functions

    def config(self):
        print("i5, 8gb, 512gb")

# Now crating an object
# comp1 # we can't simply say comp1 we have to specify it's type
# Example:
# a = 5 # Now a is type of Integer
# same as that

comp1 = Computer()

print(type(comp1))

# now we'll see how to call or execute method of an object
comp1.config()

# also can do as following
Computer.config(comp1)