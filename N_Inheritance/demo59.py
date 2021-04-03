# Multi Level Inheritance

class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):  # class B extended class A.
    a, b = 100, 200

    def m2(self):
        print(self.a + self.b)


class C(B):
    i, j = 1, 2

    def m3(self):
        print(self.i + self.j)


# b = B()
# b.m1()
# b.m2()
c = C()
c.m1()
c.m2()
c.m3()
