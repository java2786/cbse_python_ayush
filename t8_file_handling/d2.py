file = open("why", "r")

# data = file.read()
# data = file.read(10) # n characters read
# print(data)

# line = file.readline()
# print(line)

# line = file.readline()
# print(line)

lines = file.readlines()
# print(lines)

for line in lines:
    print(line, end="")


# always close file after use
file.close()