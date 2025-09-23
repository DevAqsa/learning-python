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

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("BMW")

# print(car1.start())
# print(car1.color)


# Inheritance
# Types
# · Single Inheritance --> base class to derived class 

# · Multi-level Inheritance --> base class --> derived class --> derived class

# · Multiple Inheritance --> derived class and this derived class can inherit the multiple base class properities

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B): #inhertance
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# ------------------------------------------

# Super method
# super( ) method is used to access methods of the parent class.

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type) # when we write the super means the parent inheritance

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

# class method
# A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & generally for utility.

# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         # Person.name = name
#         self.__class__.name = "aqsa"

# p1 = Person()
# p1.changeName("aqsa")
# print(p1.name)
# print(Person.name)


# class Person:
#     name = "anonymous"

    # def changeName(self, name):
    #     # Person.name = name
    #     self.__class__.name = "aqsa"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = Person()
# p1.changeName("aqsa")
# print(p1.name)
# print(Person.name)


# Property
# We use @property decorator on any method in the class to use the method as a property.

# class Student:
#     def __init__(self, phy, chem, math) :
#         self.phy = phy
#         self.chem = chem
#         self.math = math

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) /3) +"%"
#     @property 
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) /3) +"%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)

# note :  more decorator --> getter and setter 

# -----------------------------------------------------

# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning according to the context.

# Operators & Dunder functions

#a + b  addition  a. add (b)

# a - b subtraction a. sub (b)

# a * b multiplication a. mul (b)

# alb division  a. truediv (b)
 
# a % b addition a. mod (b)

# print(1 + 2) #3
# print("apna" + "college") #concatenate
# print([1, 2, 3] + [4, 5, 6]) #merge

class Complex:
   
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2): #dunder function
        newReal = self.real + num2. real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(5, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

