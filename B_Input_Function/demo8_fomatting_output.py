name = 'John'
age = 25
sal = 100000.25

# approach 01:
print(name, age, sal)

# approach 02:
print("name: ", name)
print("age: ", age)
print("salary: ", sal)

# approach 03: using percentile(%) operator
print("name:%s Age:%d salary:%g" % (name, age, sal))

# approach 04: value
print("name:{} age{} salary{}".format(name, age, sal))

# approach 05: index & value
print("name:{0} age{1} salary{2}".format(name, age, sal))

# approach 06:
print(f"name is {name}, age is {age} & salary is {sal} TK")
