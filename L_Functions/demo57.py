# returning more than one value from a function

def bigger(a, b):
    if a > b:
        return a, b
    else:
        return b, a


i = bigger(120, 130)
print(i)    # more than one value will be returned as a tuple
print(type(i))