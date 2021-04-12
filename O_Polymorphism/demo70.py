class Bird:
    def Fly(self, name=None):
        if name == 'parrot':
            print('can fly')
        if name == 'penguin':
            print('can not fly')
        if name is None:
            print('no input')


obj = Bird()
obj.Fly('parrot')
