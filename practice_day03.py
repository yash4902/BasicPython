# file1 = open("new.txt","r")

# content = file1.read()
# print(content)

# line = file1.readline()
# print(line)

# lines = file1.readlines()
# print(lines)

# file2 = open("new2.txt","w")

# print(file2.write("Hello I'm from new2"))

# content = file2.write("\nHello I'm also from new2")
# print(content)


# fo = open("new3.txt","w")
# fo.write("Hello I'm form new3.txt\nI'm new simple file\n")
# fo.close()

# fo = open("new4.bin","wb")
# data = b"Hello I'm from new4.bin"
# fo.write(data)
# fo.close()


# fo = open("new3.txt","a")
# text = "Hello I'm from append file and it's append text"
# fo.write(text)
# fo.close()


# fo = open("new4.bin",'w+')
# text = "This is a cat cage"
# fo.write(text)
# fo.seek(10,0)
# fo.write("rat")
# fo.close()



# fo = open("foo.txt","r")
# text = fo.read(20)
# print(text)
# fo.close()



# fo1 = open("new4.bin","wb")
# data = b"hello world"
# fo1.write(data)
# fo1.close()

# import os
# os.remove("new.txt")
# os.rename("new2.txt","New2.txt")
# os.mkdir("New.txt") create the new folder 
# os.chdir("/bin/python3") change the directory
# os.getcwd() give the information about what directory you are working in 
# os.rmdir("New.txt") remove the directory from the folder 











# class Employee:
#     def __init__(self, name="Bhavna",age=21):
#         self.name = name
#         self.age = age
#     def displayEmployee(self):
#         print("Name : ",self.name, "Age : ",self.age)

# print(Employee.__doc__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__bases__)
# print(Employee.__dict__)







# class Employee:
#    empCount = 0
#    def __init__(self, name, age):
#       self.__name = name
#       self.__age = age
#       Employee.empCount += 1
#    def showcount(self):
#          print (self.empCount)
#    counter=classmethod(showcount)

# e1 = Employee("Bhavana", 24)
# e2 = Employee("Rajesh", 26)
# e3 = Employee("John", 27)

# e1.showcount()
# Employee.counter()









# class Employee:
#     empCount = 0 
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#         Employee.empCount += 1
    
#     @staticmethod
#     def showcount():
#             print(Employee.empCount)
#             return
#     counter = staticmethod(showcount)
     
# e1 = Employee("Bhavana",24)
# e2 = Employee("rajesh",25)
# e3 = Employee('Yash',26)


# e1.showcount()


# class Animal:
#     def __init__(self):
#         self.name = "Dog"
#         self.age = 5
    
# a1 = Animal()
# print("Name: {}".format(a1.name))
# print("Age: {}".format(a1.age))





# class Employee:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 

# e1 = Employee("yash",21)
# e2 = Employee("abc",22)

# print("Name: {}".format(e1.name))
# print("Age: {}".format(e1.age))
# print("Name: {}".format(e2.name))
# print("Name: {}".format(e2.age))


# class Employee:
#    def __init__(self, name, age, salary):
#       self.name = name # public variable
#       self.__age = age # private variable
#       self._salary = salary # protected variable
#    def displayEmployee(self):
#       print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

# e1=Employee("Bhavana", 24, 10000)

# print (e1.name)
# print (e1._salary)
# print (e1._Employee__age)






# class Employee:
#    def __init__(self, name, age):
    #   self.__name = name
    #   self.__age = age
# 
#    def get_name(self):
    #   return self.__name
#    def get_age(self):
    #   return self.__age
#    def set_name(self, name):
    #   self.__name = name
    #   return
#    def set_age(self, age):
    #   self.__age=age
#    name = property(get_name, set_name,"name")
#    age = property(get_age,set_age,"age") 
# 
# e1=Employee("Bhavana", 24)
# print ("Name:", e1.name, "age:", e1.age)
# e1.set_name("Yash")
# e1.set_age(21)
# print ("Name:", e1.name, "age:", e1.age)



# class Parents: 
#     def __init__(self):
#         self.attr = 100
#         print("Calling parents constructor")
    
#     def parentsMethod(self):
#         print("calling parents mehtod")
#     def set_attr(self,attr):
#         self.attr = attr

#     def get_attr(self):
#         print("Parents attribute : ",self.attr)

# class Child(Parents):
#     def __init__(self):
#         print("caaling child constructor ")
#     def childMethod(self):
#         print("calling child method")

# c = Child()
# c.childMethod()
# c.parentsMethod()
# c.set_attr(10)
# c.get_attr()


# class division:
#     def __int__(self,a,b):
#         self.n = a
#         self.d = b
#     def divide(self):
#         return self.n/self.d

# class modules:
#     def __init__(self,a,b):
#         self.n = a
#         self.d = b
#     def mod_divide(self):
#         return self.n % self.d
    
# class calculator(division,modules):
#     def __init__(self,a,b):
#         self.n = a
#         self.d = b
#     def div_and_mod(self):
#         divval = division.divide(self)
#         modval = modules.mod_divide(self)
#         return(divval,modval)


# x =calculator(12,7)
# print("division: ",x.divide())
# print("mod_division: ",x.mod_divide())
# print("div and mod: ",x.div_and_mod())







# class Parent: # define parent class
#    def myMethod(self):
#       print ('Calling parent method')

# class Child(Parent): # define child class
#    def myMethod(self):
#       print ('Calling child method')

# c = Child() # instance of child
# c.myMethod() # child calls overridden method






# class example:
#    def add(self, a = None, b = None, c = None):
#       x=0
#       if a !=None and b != None and c != None:
#          x = a+b+c
#       elif a !=None and b != None and c == None:
#          x = a+b
#       return x

# obj = example()

# print (obj.add(10,20,30))
# print (obj.add(10,20))


# 
# from multipledispatch import dispatch 
# class example():
    # @dispatch(int,int)
    # def add(self,a,b):
        # x = a + b
        # return x
    # @dispatch(int,int,int)
    # def add(self,a,b,c):
        # x = a + b + c
        # return x 
    # 
# e = example()
# 
# print(e.add(1,2))
# print(e.add(1,2,3))

# from os import name


# class Student:
#     def __init__(self,name = "Yash",marks=90):
#         self.name = name 
#         self.marks = marks
# s1 = Student()
# s2 = Student("Bharat",89)

# print("Name: {}, Marks: {}".format(s1.name, s1.marks))
# print("Name: {}, Marks: {}".format(s2.name, s2.marks))


# class Employee:
#     def __init__(self,name ="yash",age = 21)
#         self.name = name 
#         self.age = age 
# e1 = Employee()
# e2 = Employee("Bharat",22)

# print("Name: {}, Age: {}".format(e1.name,e1.age))
# print("Name: {}, Age: {}".format(e2.name,e2.age))


# def circle(r):
#     import math
#     area = math.pi*math.pow(r,2)
#     return area


# print(circle(5))

# from enum import Enum

# class subjects(Enum):
#     ENGLISH = 1
#     MATHS = 2
#     SANSKRIT = 3
#     SCIENCE = 4
# obj = subjects.ENGLISH
# obj1 = subjects.MATHS
# obj2 = subjects.SANSKRIT
# obj3 = subjects.SCIENCE

# print(obj.name,obj.value)
# print(obj1.name,obj1.value)
# print(obj2.name,obj2.value)
# print(obj3.name,obj3.value)

# for sub in subjects:
#     print(sub.name, sub.value)



# try:
#    fh = open("New2.txt", "w")
#    fh.write("This is my test file for exception handling!!")
# except IOError:
#    print ("Error: can\'t find file or read data")
# else:
#    print ("Written content in the file successfully")
#    fh.close()



# try:
#    fh = open("new3.txt", "w")
#    try:
#       fh.write("This is my test file for exception handling!!")
#    finally:
#       print ("Going to close the file")
#       fh.close()
# except IOError:
#    print ("Error: can\'t find file or read data")





# def functionName( level ):
#     if level < 1:
#         raise Exception(level)
#     return level

# # try:
# #     l = functionName(10)
# #     print("level = ",l)
# # except Exception as e:
# #     print("error in level argument",e.args[0])



# try: 
#     open("New.txt")
# except OSError:
#     raise RuntimeError("Unable to handle error")




# try:
    # open("New.txt")
# except OSError as exc:
    # raise RuntimeError from None


# try: 
#     try:
#         raise ValueError("ValueError")
#     except ValueError as e1:
#         raise RuntimeError from e1
# except TypeError as  e2:
#     print("The Exception was",repr(e2))
#     print("Its __context__ was ",repr(e2.__context__))
#     print("Its __cause__ was ",repr(e2.__cause__))


# a = 0 
# b = 1
# try: 
#     print(a/b)
# except Exception:
#     print("General  Exception")
# finally:
#     print("inside outer finally block")



# a = 10 
# b = 0


# try:
#     print("this is outer try block ")
#     try:
#         print(a/b)
#     except KeyError:
#         print("KeyError")
#     finally:
#         print("Inside inner finally block")

# except ZeroDivisionError:
#     print("Division by 0")
# finally:
#     print("Inside outer finally block")




# class MyException(Exception):
#    "Invalid marks"
#    pass
   
# num = 101
# try:
#    if num <0 or num>100:
#       raise MyException
# except MyException as e:
#    print ("Invalid marks:", num)
# else:
#    print ("Marks obtained:", num)




# import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This message will get logged')


# import logging

# logging.basicConfig(filename='logs.txt', filemode='w', level=logging.DEBUG)
# logging.warning('This messagewill be saved to a file')  


# import logging

# logging.basicConfig(level=logging.DEBUG)
# marks = 100
# logging.error("Invalid marks:{} Marks must be between 0 to 100".format(marks))
# subjects = ["Phy", "Maths"]
# logging.warning("Number of subjects: {}. Should be at least three".format(len(subjects)))






# print("enter marks out of 100")
# num = 75
# assert (num>=0 and num<=100)
# print("marks obtained: ",num)

# num = 125
# assert num >= 0 and num<=100
# print("marks obtained: ",num)




# try: 
#     num = int(input("enter the number: "))
#     assert (num>=0) ,"Only non negative numbers accepted"
#     print(num)
# except AssertionError as msg:
#     print(msg)