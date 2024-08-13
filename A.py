'''t = ['a', 'b', 'c']
x = t.pop(2)  # removing of element
x = t.pop()   # if index is not specified it eliminates last one
print(t)      # for index () is used
print(x)      # pop method displays the removed element'''
from functools import reduce

'''# the del operator
a=[1,2,3,4]   # del doesn't return the removed value
del a[1]      # index is represented in [].
del a[1:3]     # we can use slicing for removing a sequence of elements
print(a)'''

'''# remove and append
a=[1,2,3,4,5]
a.remove(5)   #append adds at the end ,remove removes it 
print(a)      
a.append(6)
print(a)'''

'''# index
s=[1,2,3,4,5,6,7]
print(s.index(4))'''

'''#insert
m=[1,2,3,4]
m.insert(4,5)
print(m)'''

'''# reverse
t=[6,3,7,0,3,7,6,0]
#t.reverse() #changes the list(updates the value)
t=t.[::-1]
print(t)'''

'''a=int(input("Enter the first number"))
b=int(input("enter the second number"))
c=a+b
print(c)'''

'''import math
radius=int(input("Enter the radius"))
print("Area of the circle :",round(math.pi,2)*radius*radius)
print("circumference of the circle:"2*round(math.pi,2)*radius)'''

'''p=int(input("Enter principal amount:"))
t=int(input("Enter time:"))
r=int(input("Enter rate:"))
SInt=p*t*r/100
print("the simple intrest:",Sint)'''

'''for i in range(1,10,2):
    print(i,i*i,i*i*i)'''

'''#formatting
rno=23
per=89
print("my roll no is:{} and my percentage is:{}".format(rno,per))
print("my roll no is:{} and my percentage is:{:.2f}".format(rno,per))'''

'''x=10
a=bin(x)
b=hex(x)
c=oct(x)
print(a,b,c)'''

'''
#evalute 
a=9
b=12
print(eval("a-b"))'''

'''k = int(input())
sum = 0
while k>0:
    l = k % 10
    sum = sum + l
    k = k // 10
print(sum)'''

'''
# priority order 
meal = "fruit"
money = 0
if meal == "fruit" or meal == "sandwich" and money >= 2:
    print("Lunch is being delivered")
else:
    print("lunch is not being delivered")   #priority works '''

'''class Student:
    id = 1
    name = "rishika"

    def display(self):
        print(f"my name is {self.name} and id is {self.id}")


r = Student()
r.display()'''

'''class Laptop:
    def __init__(self, colour, model):
        self.colour = colour
        self.model = model

    def display(self):
        print(f"colour is {self.colour} and the model is {self.model}")


L1 = Laptop("grey", 'U 12TH GEN envy')
L2 = Laptop("blue", "13 th gen pavallion")

L1.display()
L2.display()'''

'''def square(num):
    return num * num


data = [1, 2, 3, 4, 5]
res = map(square, data) # map
print(list(res))'''

'''def verify(age):
    return age > 18


data = [23, 69, 79, 891, 2, 3, 4]
res = list(filter(verify, data)) # filter
print(res)'''

# def perform(a,b):# A=STORAGE # from function tools import reduce
'''def perform(result, num):
    return result * num


data = [1, 2, 3, 4, 5]
res = reduce(perform, data)
print(res)'''


def antique(result, num):
    if num % 2 == 0:
        return result + (2 * num)
    else:
        return result + (3 * num)


num = [1, 2, 3]
res = reduce(antique, num)
print(res)
