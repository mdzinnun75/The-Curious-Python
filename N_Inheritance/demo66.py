class A:
    def __init__(self):
        print('constructor from A')


class B(A):
    def __init__(self):
        print('constructor from B')
        super().__init__()  # calls the parent class constructor
        A.__init__(self)    # calls the parent class constructor


b1 = B()
