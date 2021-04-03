friends = {
    'tom': '111-222-333',
    'jerry': '666-222-999',
}

print(friends)
print(friends['tom'])
# print(friends['111-222-333'])

# adding a element
friends['bob'] = '222-3333-444'

# Modify element
friends['bob'] = '333-555-999'
print(friends)

# deleting element
del friends['bob']
print(friends)
