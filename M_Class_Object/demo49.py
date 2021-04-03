class MyClass:
    def __del__(self):
        print('Destroyed')


obj = MyClass()
obj1 = MyClass()

del obj
