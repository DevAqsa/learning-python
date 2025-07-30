# loops in python -- repeat the instructions 

# while loop and for loop

# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1

#the variable with the help of we iterate is called iterator and the circle is called iteration


# print 1 to 5 numbers
# i = 1 
# while i <= 5:
#     print(i)
#     i += 1


# practice questions 

# q no 1 

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# q no 2

# i = 100
# while i >=1: stopping condition
#     print(i)
#     i -= 1

# q no 3

# n = int(input("give me the table of this number :"))
# i = 1
# while i <= 10: #stoping condition
#     print(n * i)
#     i += 1

# q no 4

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] #traverse

# i = 0
# while i < len(nums):
#     print(nums[i]) #nums[0], nums[1], nums[2]...
#     i += 1

# q no 5

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36
# i = 0 #initialization
# while i < len(nums):
#     if(nums[i] == x):
#         print("found" ,i  )
#         break
#     else:
#         print("findings...")
#     i +=1

# break and continue keyword

# j = 1
# while j <=5:
#     print(j)
#     if(j ==3):
#         break
#     j += 1

# print("end of loop")    

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue #skip
#     print(i)
#     i +=1

# list = [1,2,3]

# for val in list:
#     print(val)


# str = "aqsa mumtaz"

# for chr in str:
#     print(chr)
# else: #we mostly use this else with break 
#     print("end")

# practice again questions
# q no 1
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for val in nums:
#     print(val)

# q no 2 
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0
for el in nums:
    if (el == x):
        print("num found at idx: ", idx)
    idx +=1



