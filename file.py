# open a file

# f = open("demo.txt", "r")

# data = f.read()

# print(data)

# print(type(data))

# f.close()

# reading a file

# f = open("demo.txt", "r")

# data = f.read()
# data = f.readline()

# print(data)

# f.close()

# if we dont have the further line for reading so then the print the empty line 


# writing a file 

# a --> append-->  ad at the end 

# f = open("demo.txt", "a")

# f.write("\nthen i'll move to nodejs")

# f.close()

# if we dont have file but we open the file then the python created that file 
# f = open("sample.txt", "w" )

# f.close()

# f = open("sample.txt", "r+")

# f.write("hi i'm aqsa")

# f.close()

# modez

# r+ read and overwrite (pointer at start) no truncate

# w+ "" truncate

# a+ read and append(pointer at end) no truncate

# with syntex 

# with open ("sample.txt", "r") as f :
#     data = f.read()
#     print(data)

# with open("sample.txt", "w") as f:
#     f.write("here is the new data")

# deleting files 

import os

os.remove("sample.txt")
