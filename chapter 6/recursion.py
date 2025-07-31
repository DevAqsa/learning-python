# when a function calls itself repeatedly

# def show(n):
#     print(n)

# show(9)

# recursive function
# def show(n):
#     if(n == 0): #base case
#         return
#     print(n)
#     show(n-1)

# show(5)


# n! = (n-1)! * n   recurance relatiopn 

# def fact(n):
#    if( n== 1 or n == 0):
#        return 1
#    return fact(n-1) * n

# print(fact(4))


# question 1 

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(10)
# print(sum)

# Question 2

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "apple", "bnanan", "peach"]

print_list(fruits)
