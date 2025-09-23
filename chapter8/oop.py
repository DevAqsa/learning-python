#  procedural programming 

# resueability --> functional prpgramming --> increase
# redundancy --> oop --> decrease

# oop --> class and object

#when we save the any data in the class and objects then these are called attributes or variables.

# class Student : #always use the capistal letter for class name
#     college_name = "abc college"
#     name = "anonymous" #class attribute
   #default constructor
#    def __init__(self): #constructor take the parameter called self
#     pass
   
    #parameterized constructor
    # def __init__(self, name, marks): #constructor take the parameter called self
    #     self.name = name  #obj attribute > class attribute --> because the priority of the object is higher then class
    #     self.marks = marks

#constructor call everytime when the object created   
  
#how object created is this 
# o1 = Student("aqsa", 90) #these parenthesis here for constructor calling 
# print(o1.name, o1.marks)

# print(o1.name)



# o2 = Student("sana", 89)
# print(o2.name, o2.marks)

# one more example

# class Car:  #constructor CALLed when the object is created 
#     color = "purple"
#     range = 233445

# car1 = Car()
# print(car1.color)
# print(car1.range)

# ------------------Methods------------------

# class collection of two things called data(attributes) and methods
# attributes --> properitites and methods --> how it works functions

# class Student : 

    # parameterized constructor
    # def __init__(self, name, marks): #constructor take the parameter called self
    #     self.name = name  #obj attribute > class attribute --> because the priority of the object is higher then class
    #     self.marks = marks

    # #methods
    # def welcome(self): 
    #     print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("sana", 87)
# s1.welcome()
# print(s1.get_marks())

#static methods --> these not used the parameters and work at class level

class Student:
    @staticmethod  #decorator --> change the behavious of the function

    def hello():
        print("hi")


# Four pillars of OOps

# ->Abstraction  ->encapsulation  ->inheritance ->polymorphism

# ->Abstraction --> hide the unnecessary details just show the essential features to the user

# ->Encapsulation --> wrapping data and functions into single unit (object) capsule




