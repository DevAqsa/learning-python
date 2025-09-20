# dell keyword
# used to delete the object properities or object itself
# del s1.name
# del s1

# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("aqsa")
# print(s1.name)
# del s1.name
# print(s1.name)

# Private(like) attributes and methods 

# Conceptual Implementations in Python
# Private attributes & methods are meant to be used only within the class and are not
# accessible from outside the class. 

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # __ can make the private so that we cannot access this outside of the class


# acc1 = Account("12345", "avbcdd")

# print(acc1.acc_no)
# print(acc1.acc_pass)

# Inheritance
# When one class(child/derived) derives the properties & methods of another class(parent/base).

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("BMW")

print(car1.start())
print(car1.color)


# Inheritance
# Types
# · Single Inheritance --> base class to derived class 

# · Multi-level Inheritance --> base class --> derived class --> derived class

# · Multiple Inheritance --> derived class and this derived class can inherit the multiple base class properities
# ------------------------------------------

# Super method
# super( ) method is used to access methods of the parent class.

# class method
# A class method is bound to the class & receives the class as an implicit first argument.

# Note - static method can't access or modify class state & generally for utility.

class Student:
    @classmethod  #decorator
    def college( cls ):
        pass
