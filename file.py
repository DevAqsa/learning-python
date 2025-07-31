# open a file

# f = open("demo.txt", "r")

# data = f.read()

# print(data)

# print(type(data))

# f.close()

# reading a file

f = open("demo.txt", "r")

# data = f.read()
data = f.readline()

print(data)

f.close()