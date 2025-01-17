# Python doesn't directly support for abstraction
# But it does indirectly through abc module/class

# abstract method => method which only have declaration and not body
# abstract class => class which has abstract methods
#                   we can not create objects of abstact class

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    pass

# this will throw an error we can't instantiate abstract class object
# comp1 = Computer()

# this will also throw an error causing Can't instantiate abstract class Laptop without an implementation for abstract method 'process'
# lap = Laptop()

class Laptop(Computer):
    def process(self):
        print(f"Executing process")

lap = Laptop()
lap.process()

# it is upto us or design that we should use abstract class or not in our code