# question 1 
# f = open("ptactice.txt", "w")

# f.write("Hi everyone \nwe are learning File I/O \n using Java \n i like programming in Java")

# f.close()

# question 2

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)


# with open("practice.txt", "w") as f:
#     data = f.write(new_data)

# question no 3 

# word = "learning"

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("not Found")

# question no 4 

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1 

# print(check_for_line())
     

# question 05

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range (len(data)):
        if (data[i] == ","):
            print(num)
            num = ""
        else:
            num += data[i]