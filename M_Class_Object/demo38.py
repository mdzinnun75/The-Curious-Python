x, y = 5, 15    # Global Variable


class MyClass:
    a, b = 100, 200  # Class Variable

    def add(self):
        print(self.a + self.b)  # to use class var, we must use 'self' keyword

    def multiplication(self):
        print(self.a * self.b)

    def add2(self, m, n):   # local var
        print(m + n)

    def add3(self):    # accessing global variables
        print(x + y)



mc = MyClass()
mc.add()
mc.multiplication()
mc.add3()
mc.add2(5, 6)