class MyClass:
    def m1(self):
        print('this is m1 method')
        self.m2(100)    # 'self' keyword to call m2 method

    def m2(self, a):
        print("this is m2 method", a)
        self.m1()


o1 = MyClass()
o1.m1()