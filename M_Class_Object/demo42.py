# constructor __init__
class MyClass:
    def m1(self):
        print("good morning")

    def __init__(self):  # constructor uses __init__
        print('this is a constructor')


o1 = MyClass()
o1.m1()  # constructor will be called automatically
