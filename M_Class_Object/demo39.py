a, b = 15, 25   # global variable


class MyClass:
    a, b = 10, 20   # class variable

    def add(self, a, b):
        print(a + b)    # accessing local variables
        print(self.a + self.b)  # accessing class variables
        print(globals()['a'] + globals()['b'])  # accessing global variables


mc = MyClass()
mc.add(5, 10)