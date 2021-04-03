list1 = [11, 33, 44, 66, 88, 29]

# add a element at the end
list1.append(44)
print(list1)

# remove the last element, if position is given it removes that value & returns it
list1.pop()
print(list1)
list1.pop(5)
print(list1.count(44))

# add elements from a different list
list2 = [30]
list2.extend(list1)
print(list2)

# returns the position of a given value
print(list1.index(33))

# insert a value at the given position
list1.insert(0, 22)
print(list1)

# removes the given value
list1.remove(22)
print(list1)

# reverse the list
list1.reverse()
print(list1)

# sort the list
list1.sort()
print(list1)
