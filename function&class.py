






# Encapsulation of OOPS

class bankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw (self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Unsuficient Account")

account = bankAccount(1000)



account.deposite(1200)

print(account.get_balance())

account.withdraw(500)

print(account.get_balance())



class Car:
    def __init__(self, make , model):
        self.__make = make
        self.__model = model
    
    def xyx(self):
        print(f"Car: {self.__make}, {self.__model}")


# my_car = Car("Toyota","Supra")
my_car = Car("abc","cde")
my_car.xyx()




# Polymorphism Method of OOPS

import math 

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side*2
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2

triangle = Triangle(3,1)
print(triangle.area())


square = Square(23)
print(square.area())


circle = Circle(23)
print(circle.area())


    












