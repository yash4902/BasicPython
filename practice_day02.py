# # # # from operator import le
# # # # import re

# # # # from cv2 import divSpectrums


# # # # zen = '''
# # # # Beautiful is better than ugly.
# # # # Explicit is better than implicit.
# # # # Simple is better than complex.
# # # # Complex is better than complicated.
# # # # '''
# # # # for char in zen:
# # # #     if char not in "aeiou":
# # # #         print(char ,end="")



# # # # number = [1,2,3,4,5,6,7,8,9,10,12,14,22,24,]
# # # # for i in number:
# # # #     if i%2==1:
# # # #         print(i)

# # # # for i in number:
# # # #     if i%2==0:
# # # #         print(i)



# # # # for num in range(4):
# # # #     print(num,end=",")

# # # # for num in range(1,11):
# # # #     print(num+1, end=",")



# # # # # var = "0"
# # # # # while var.isnumeric()==True:
# # # # #     var = input("Enter your number..")
# # # # #     if var.isnumeric()==True:
# # # # #         print(f"Your input value is {var} numeric value")
# # # # # print("You are not entering the numeric value")


# # # # count = 0
# # # # while count<5:
# # # #     count+=1
# # # #     print("Iterations no {}".format(count))
# # # # else:
# # # #     print("while loop over. you are in else block")
# # # # print("End of the while loop")



# # # # var = "0"
# # # # while var.isnumeric()==True:
# # # #     var = input("Enter the number... ")
# # # #     if var.isnumeric()==True:
# # # #         print("Your numeric is",var)
# # # # print("End of the while loop")




# # # # for letter in "Python":
# # # #     if letter=="h":
# # # #         break
# # # #     print("Current Letter is", letter)


# # # # var = 10 
# # # # while var >0:
# # # #     print("Current variable value is: ",var)
# # # #     var = var -1
# # # #     if var == 5:
# # # #         break
# # # # print("Your loop is over")










# # # # var =  10
# # # # while var > 0:
# # # #     print("Your Current variable value is: ",var)
# # # #     var = var - 1
# # # #     if var == 5:
# # # #         break
# # # # print("Your loop is over.")










# # # # var = "Python"
# # # # for letter in var:
# # # #     if letter == "h":
# # # #         continue
# # # #     print("Your var values is: ",letter)

# # # # var = 10
# # # # while var > 0:
# # # #     var = var - 1
# # # #     if var == 5:
# # # #         continue
# # # #     print("Current var value is:", var)


# # # def prime_factor(n):
# # #     factor = []
# # #     divisor = 2
# # #     while divisor <= n:
# # #         if n %divisor == 0:
# # #             factor.append(divisor)
# # #             n //= divisor
# # #         else:
# # #             divisor += 1
# # #     return factor

# # # n = int(input("Enter the number: "))
# # # print(f"Prime factor of the {n}: {prime_factor(n)}")





# # # for letter in 'Python':
# # #     if letter == "h":
# # #         continue
    
# # #     print("Current letter: ", letter)
# # # print("end of the loop")

# # a = [1,2,3,4]
# # b = [5,6,7,8]

# # for x in a:
# #     for y in b:
# #         print(x,"X",y," = ",x*y)


# # i = 2 
# # while (i < 100):
# #     j = 2 
# #     while (j <= (i/j)):
# #         if not(i%j): break
# #         j = j + 1
# #     if (j > i/j):
# #         print (i, "is prime")
# #     i = i + 1 
# # print("end the loop")




# # def custom_len(sequance):
# #     count = 0 
# #     for _ in sequance:
# #         count += 1
# #     return count


# # list = [1,23,4,3,35,3,43,442,3]
# # print("The list of length is: ",custom_len(list))


# # def custom_sum(sequance):
# #     count = 0
# #     for element in sequance:
# #         count += element
# #     return count
# # print("the list of sum is:",custom_sum(list))
# # print("the list of sum is:",sum(list))



# # def percentage(phy,maths,chem,maxmarks=300):
# #     val = ((phy+maths+chem)*100)/maxmarks
# #     return val

# # result = percentage(100,89,100)
# # print(result)



# # def division(num, den):
# #    quotient = num/den
# #    print ("num:{} den:{} quotient:{}".format(num, den, quotient))

# # division(num=5,den=10)


# # def add(*args):
# #     s = 0
# #     for x in args:
# #         s = s + x
# #     return s

# # result = add(10,23,24,345,345)
# # print(result)

# # result = add(-12,23,43,12)
# # print(result)


# # import math 
# # # print("Square root of 100: ", math.sqrt(37))
# # # 
# # # print(math.ceil(4.3))

# # # print(math.floor(4.9))
# # # 
# # # print(math.trunc(4.9))
# # # 
# # # n = int(input("enter the number: "))
# # # print(math.factorial(n))
# # # 
# # # print(math.exp(0))

# # # print(math.log(8,2))
# # # 
# # # print(math.log10(20))

# # # print(math.pow(2,10))

# # # print(math.sin(math.pi/2))

# # # print(math.cos(math.pi))

# # # print(math.tan(math.pi/4))

# # # print(math.degrees(math.pi))

# # # print(math.radians(180))

# # # print(math.sqrt(23))

# # # print(math.isfinite(5.0))

# # # print(math.isnan(float('nan')))

# # # print(math.gcd(24,36))

# # # print(math.hypot(3,4))

# # # print(math.pi)

# # # print(math.e)


# # # Tuple ----------
# # # t1 = (1,2,3,4)
# # # t2 = (5,6,7,8)
# # # t3 = t1 + t2
# # # print(t3)

# # t1 = (1,2,3,4)
# # t2 = (5,6,7,8)
# # # t1 += t2
# # # print(t1)

# # t2 += t1 
# # print(t2)


# # set  = { 'Gujarat':"Gandhinagar","Karnataka":"Bengaluru","Maharastra":"Pune"}
# # print("Capital of Gujarat is : ",set.get("Gujarat"))
# # print("Capital of Haryana is : ",set.get("Haryana","Not Found"))




# # marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
# # print ("marks dictionary before update: ", marks)
# # # marks['Krishan'] = 74
# # # marks["Harsh"] = 98
# # # print ("marks dictionary after update: ", marks)
# # marks1 = {"Savita":67, "Imtiaz":88, "Laxman":91}
# # marks.update(marks1)
# # print("marks dictionary after update: ",marks1)




# import array as arr 
# a = arr.array("i",[1,2,3])
# print(type(a),a)


# a = arr.array("u","yash")
# print(type(a),a)


# a = arr.array("d",[1.2,23.04,21.50])
# print(type(a),a)


# print(a[1])

# a[0] = 22.22
# print(a[0])

# a.append(29.00)
# print(a[3])



# a = arr.array("i",[1,2,3,4])
# a.insert(3,7)
# print(a)


# b = arr.array('i',[5,6,7,8,9])
# a.extend(b)
# print(a)

# a.remove(2)
# print(a)

# a.pop(7)
# print(a)







name = input()
import sys
name = sys.stdin.readline()
print(name)