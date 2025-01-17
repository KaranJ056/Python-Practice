# Concept behind it is :
# If something walks like a duck, talk like a duck and swims like a duck then it must be a duck

# means we can identify someone from it's behavior

# example:

class VsCode:
    def execute(self):
        print("\nCompiling code.....")
        print("Executing code.....")

class CustomIDE:
    def execute(self):
        print("\nChecking spelling.....")
        print("Checking syntax.....")
        print("Compiling code.....")
        print("Executing code.....")

class Laptop:

    def code(self, ide):
        ide.execute()

ide1 = VsCode()
ide2 = CustomIDE()

lap = Laptop()

lap.code(ide1)
lap.code(ide2)