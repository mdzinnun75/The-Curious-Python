# Hierarchical Inheritance --> one Parents having multiple Child
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 100, 200

    def m2(self):
        print(self.a + self.b)


class C(A):
    i, j = 1, 2

    def m3(self):
        print(self.i + self.j)


b = B()
b.m1()

c = C()
c.m1()
c.m3()
