class MyClass():
    def __init__(self):
        self.input = ""

    def getString(self):
        self.input = input()

    def printString(self):
        print(self.input.upper())

p1 = MyClass()
p1.getString()
p1.printString()
