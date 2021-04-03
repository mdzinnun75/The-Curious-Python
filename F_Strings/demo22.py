s = 'python'

print(s.isalnum())
print('welcome'.isalpha())
print("2012".isdigit())
print('first number'.isidentifier())
print(s.islower())
print("WELCOME".isupper())
print(" ".isspace())

# searching for substring:
print(s.endswith('thon'))
print(s.startswith('py'))
print(s.find('th'))
print(s.find('on'))
print(s.rfind('h'))     # returns the highest index of a string
print(s.count('h'))
