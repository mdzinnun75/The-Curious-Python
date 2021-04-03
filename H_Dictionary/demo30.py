values = {'b': 200, 'c': 300, 'a': 100}
values1 = {'a': 100, 'b': 200, 'c': 300}
values3 = {'d': 100, 'e': 200, 'f': 300}

for x in values:
    print(x, ":", values[x])

print(len(values))
print('d' in values)
print('d' not in values)

print(values == values1)
print(values1 == values3)

