# super keyword
# accessing variables from parent class
class A:
    x, y = 11, 22


class B(A):
    i, j = 20, 30

    def m1(self, x, y):
        print(x + y)
        print(self.i + self.j)
        print(self.x + self.y)


b = B()
b.m1(3, 1)
