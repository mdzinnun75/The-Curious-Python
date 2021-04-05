# super keyword
# accessing variables with same name from parent class
x, y = 15, 20


class A:
    x, y = 11, 22


class B(A):
    x, y = 20, 30

    def m1(self, x, y):
        print(x + y)
        # print(self.x + self.y)
        print(self.x + self.y)
        print(super().x + super().y)
        print(globals()['x'] + globals()['y'])


b = B()
b.m1(3, 1)
