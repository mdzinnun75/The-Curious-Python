"""
class is a logical entity which contains logic
Class contains logic & variable
logic should be included within method

An object is physical entity which is created for a class
we can create any number of object for a class
"""


class MyClass:
    def myfunc(self):
        pass

    def display(self, name):
        print("name : ", name)


mc = MyClass()      # mc is object reference variable
mc.display('zinnun')
