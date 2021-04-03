class MyClass:
    def m1(self):
        print("instance method")

    @staticmethod
    def m2():   # static method doesn't have 'self' keyword like general method, given 'self' would be considered as parameter.
        print("static method")

# mc = myClass()
# mc.m1()


MyClass.m2()