class MyClass:
    def __init__(self, val1, val2):
        print(val1)  # local variable
        print(val2)
        self.val1 = val1  # making local variable as class variable
        self.val2 = val2  # making local variable as class variable

    def add(self):
        print(self.val1 + self.val2)


obj = MyClass(30, 40)
# o1.values(10, 20)
obj.add()
'''
    def values(self, val1, val2):   # val1, val2 are local method
        print(val1)     # local variable
        print(val2)
        self.val1 = val1    # class variable
        self.val2 = val2    # class variable
'''
