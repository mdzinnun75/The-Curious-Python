name = str("kiko")
print(name)

str1 = "niko"
str2 = "niko"

print(id(str1))  # 1536336923440
print(id(str2))  # 1536336923440

str2 = str2 + "to python"
print(id(str1))  # 1465639635760
print(id(str2))   # 1465640003760
