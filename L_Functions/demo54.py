xy = 100


def cool():
    # xy = 200
    global xy       # to make it global, declare it in one line & assign value in the next line
    xy = 200
    print(xy)


cool()
print(xy)