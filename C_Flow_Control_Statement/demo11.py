# single line
print("welcome") if True else print("Python")

print("welcome") if False else print("Python")
print("welcome") if 10 < 20 else print("Python")
print("welcome") if 10 > 20 else print("Python")

# multiple statement for single line
{print("welcome"), print("python1")} if True else {print("Welcome2"), print("python2")}
{print("welcome"), print("python1")} if False else {print("Welcome2"), print("python2")}



