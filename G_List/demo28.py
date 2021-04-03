for x in range(10):
    if x % 2 == 0:
        print(x)

list2 = [x for x in range(10)]
print(list2)

list2 = [x + 1 for x in range(10)]
print(list2)

list3 = [x for x in range(20) if x % 2 == 0]
print(list3)

list3 = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(list3)
