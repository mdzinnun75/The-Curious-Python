# Multiple Inheritance:

class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B:
    a, b = 100, 200

    def m2(self):
        print(self.a + self.b)


class C(A, B):
    i, j = 1, 2

    def m3(self):
        print(self.i + self.j)