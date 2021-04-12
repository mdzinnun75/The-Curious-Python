class A:

    name = 'zain'
    # def m1(self):
    #     print('this is m1 method from class A ')


class B(A):
    name = 'banna'


b1 = B()
print(b1.name)