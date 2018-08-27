"""
Q.1- Name and handle the exception occured in the following program:

a=3
if a<4:
a=a/(a-3)
print(a)
"""

print("error is ZeroDivisonError")
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("Error occurred has been handled")

"""
Q.2- Name and handle the exception occurred in the following program:
l=[1,2,3]
print(l[3])
"""

print("error is IndexError")
try:
    l=[1, 2, 3]
    print(l[3])
except IndexError:
    print("error occurred and is handled")

"""
Q.3- What will be the output of the following code:

Program to depict Raising Exception

try:
raise NameError("Hi there")  # Raise Error
except NameError:
print("An exception")
raise #To determine whether the exception was raised or not

Answer is that an exception will be printed followed by a raise error.
"""

"""
Q.4- What will be the output of the following code:
Function which returns a/b
def AbyB(a , b):
try:
c=((a+b)/(a-b))
except ZeroDivisionError:
print("a/b result in 0")
else:
print(c)
#Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

Answer:
-5.0
a/b result is zero
"""

"""
Q.5- Write a program to show and handle following exceptions:
1. Import Error
2. Value Error
3. Index Error
"""

#Import error
try:
    from time import datetime
except ImportError:
    print("Import Error handled")

#Value error
try:
    a=float("pritish")
except ValueError:
    print("Value Error handled")

#Index error
try:
    list=[1,2,3,4,5,6]
    print(list[8])
except IndexError:
    print("Index Error handled")
