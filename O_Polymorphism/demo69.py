class Human:
    def SayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('hello')


obj = Human()
obj.SayHello('zinnun')