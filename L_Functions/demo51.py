def sum(start, end):
    if start > end:
        print('start value should be greater than end value')
        return  # it'll return none
    result = 0
    for i in range(start, end + 1):
        result = result + i
    return result


s = sum(1, 5)
print(s)
