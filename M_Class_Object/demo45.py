class MyClass:
    name = 'Uddin'

    def __init__(self, name):
        print(name)     # local variable
        print(self.name)        # class variable


o = MyClass('Zinnun')
