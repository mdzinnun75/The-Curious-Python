#   passing arguments to a function

def func(i, j=100):  # assigning a default value
    print(i, j)


func(10)  # 10 100

func(20, 250)  # 10 250, default value override with a new value
