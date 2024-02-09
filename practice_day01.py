from multiprocessing.util import ForkAwareLocal
from operator import index


c = "Hello"

obj = list(c)
print(obj)

obj = tuple(c)
print(obj)

obj = set(c)
print(obj)

a = (1,2,3,4,5)

obj1 = str(a)
print(obj1)



a = 3 + 4j
b = 2 + 5j
c = a*b
print(c)

a = 5
b = 3
a*=b
print(a)


x = 10
y = 20

print("x>0 and y<0 = ", x>0 and y<0)
print("x<0 and y>0 = ", x<0 and y>0)
print("x>0 and y>0 = ", x>0 and y>0)
print("x<0 nad y<0 = ", x<0 and y<0)


a = 200
print(a<<3)
print(a>>3)

list = [1,2,3,4,5,6,7,8,9,0]
a = 1
b = 43
print ( a in list)
print( b in list )
print( a not in list)
print( b not in list )


list = {1,2,3,4}
a = list
print(a)
print(a is list)
print(a is not list)


def checkVowel(n):
    match n:
        case "a": return "Vowel alphabet"
        case "e": return "Vowel alphabet"
        case "i": return "Vowel alphabet"
        case "o": return "Vowel alphabet"
        case "u": return "Vowel alphabet"
        case _: return "Simple alphabet"

print(checkVowel("k"))




# words = ["one","two","three"]
# for i in words:
    # print(i)
# 
# n = int(input("Enter the number = "))
# for i in range(1,n+1):
#     print(i)


i = 1
while i < 6:
    print(i)
    i += 1



var = 100.5
if (var == 100):
    print("It's equal to 100")
elif (var > 0):
    print("It's greater than 100")
else:
    print("It's less than 100")



def access(user):
    match user:
        case "admin" | "manager": return "Full access"
        case "Guest": return "Guest access"
        case _: return "Not accessable"

print(access("manager"))
print(access("Guest"))
print(access("user"))



def intreset(details):
    match details:
        case[amt,duration] if(amt<10000):
            return (amt * 2 * duration) /100
        case[amt,duration] if(amt>10000):
            return (amt * 5 * duration) /100
        
print(intreset([100000,75]))


number = (13,445,33,55,67,4,23,89)
total = 0
for i in number:
    total += i
print(total)


fact = 1 
n = 10
for i in range(1, n+1):
    fact = fact*i
print("factorial of {} is {}".format(n,fact))





number = [12,343,5,6,7]
indeces = range(len(number))
for i in indeces:
    print("Index: ",i, "Number: ", number[i])


count = 0 
while count<5:
    count+=1
    print("Iteration no. {}".format(count))
print("end the while loop")


