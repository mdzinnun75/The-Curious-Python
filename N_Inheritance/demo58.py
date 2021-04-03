# Single Inheritance

class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):     # class B extended class A. Single Inheritance.
    a, b = 100, 200

    def m2(self):
        print(self.a + self.b)


b = B()
b.m1()
b.m2()