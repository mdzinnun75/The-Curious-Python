class MyClass:
    def __str__(self):
        return 'welcome'    # it must be a String, otherwise it will throw type error


obj = MyClass()
print(obj)      # calls the __str__ function. if the __str__ function is not written, this will show the memeory address of "obj"