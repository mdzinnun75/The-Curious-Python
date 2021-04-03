friends = {'tom': '111-222-333', 'jerry': '666-222-999'}

# return an item randomly & remove that
print(friends.popitem())
print(friends)

# clear() --> delete everything from a dictionary & return None
print(friends.clear())

friends = {'tom': '111-222-333', 'jerry': '666-222-999', 'jerry': '666-222-999', 'duck': '666-222-999'}  # dictionary can keep duplicate values.

# return keys in dictionary as tuples
print(friends.keys())

# return values in dictionary as tuples
print(friends.values())

# get(key)
print(friends.get('jerry'))

# pop() --> remove & return an item in a dictionary
print(friends.pop('tom'))

print(friends)