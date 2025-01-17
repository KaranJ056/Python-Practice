class Computer():
    # def __init__(self):
    #     # We can consider it as a constructor
    #     # It used to initialize objects with some value
    #     print("in init")

    # use following init method with args to pass initial values to objects
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        print("Object Initialized!")

    def config(self):
        print(f"This computer is of config {self.cpu} {self.ram} and {self.storage}")

comp1 = Computer("i5","8gb","512gb")

comp1.config()