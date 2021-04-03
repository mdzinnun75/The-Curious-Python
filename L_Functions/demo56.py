# positional & keyword arguments

def named_args(name, greeting):
    print(greeting + " " + name)


def my_func(a, b, c):
    print(a, b, c)


named_args("zinnun", "hi")  # positional arguments
named_args(name='zinnun', greeting='hi')   # keyword arguments
named_args(greeting='hi', name='zinnun')   # keyword arguments

my_func(10, 20, 30)
my_func(b=20, c=30, a=10)
my_func(30, c=10, b=20)     # positional arguments must be appeared before keyword arguments
