file = open('E:\pythonProject\The Curious Python\K_FileHandling\myfile.txt', 'a')
file.write('this is third line')

file = open('E:\pythonProject\The Curious Python\K_FileHandling\myfile.txt', 'r')
# print(file.read(10))
print(file.read())
# print(file.readline())
# list =
# print(file.readlines())


file.close()

