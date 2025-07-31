# block of code that perform a specific task called function

# def calc_sum(a, b): #these values which we pass in the funbction is called parameters
#     sum = a + b
#     print(sum)

# calc_sum(7, 19) #these values which we pass in the function when we calling then these values are called arguments 

# another syntex of function 
# def val_sum(x, y):
#     return x + y

# sum = val_sum(23, 56)
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()

# when function did not return anything then their out put will be none

# output = print_hello()
# print(output)

# average of 3 numbers

# def calc_avg(a, b , c):
#     sum = a +b +c
#     avg = sum /3
#     print(avg)
#     return avg

# calc_avg(1, 3, 5)

# there are two types of functions in python are built in functions and usr defined function 

#default parameters

# def cal_prod(a = 3, b =3):
#     print( a * b)
#     return a * b 

# cal_prod()

# practice questions 

# q no 1

# cities = ["khanewal", "multan", "lahore", "Islamabad"]
heroes = ["thor", "arisu", "usagi", "captain", "ironman"]

# def prin_len(list):
#     print(len(list))

# prin_len(cities)
# prin_len(heroes)

# q no 2

# def prin_list(list):
#     for item in list:
#         print(item, end=" ")

# prin_list(heroes)

# q no 3

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)

# q no 4

# def converter(usd_val):
#     pkr_val = usd_val * 283
#     print(usd_val, "USD =", pkr_val, "PKR")

# converter(436)

# write the function we get the even number from user then we print the even string and vice versa for odd numbers