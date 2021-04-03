# slicing operator:
list = [11, 33, 44, 66, 88]
print(list[0:5])
print(list[:2])
print(list[:-1])
print(list[2:])

# + and * operator:
list1 = [22, 44, 55, 77, 99]
list2 = list + list1
print(list2)

# 'in' or 'not in' operator:
print(55 in list2)
print(32 not in list2)

# for loop
for number in list:
    print(number)

# printing at the same line:

for numbers in list1:
    # print(numbers, end=" ")
    print(numbers, end=",")




