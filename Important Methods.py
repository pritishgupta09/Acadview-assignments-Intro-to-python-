#Q.1) Reverse a list using list methods

n=int(input("Enter the size of the list: "))
list=[]
for i in range(0,n):
    a = int(input("Enter the elements: "))
    list.append(a)
print("List is: ",list)
print("Reverse list is: ",list[::-1])

#Q.2)Print all the uppercase letters from the string

str=input("Enter a string: ")
print("Uppercase letters of the string are: ")
for i in str:
    if(i>="A" and i<="Z"):
        print(i,end ="")

#Q.3- Split the user input on comma's and store the values in a list as integers.

n1=input("Enter numbers using commas: ").split(",")
list1=[]
for i in n1:
    b = int(i)
    list1.append(b)
print("List is: ",list1)

#Q.4)Check whether string is palindromic or not

str1=input("Enter any string: ")
str2=str1[::-1]
if(str1==str2):
    print("String is palindrome")
else:
    print("String is not a palindrome")

#Q.5)Make a deepcopy of a list and write difference between shallow copy and deep copy

import copy

list2=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list3=copy.deepcopy(list2)

list2[1][0] = 'ABC'

print("Original list:", list2)
print("New list:", list3)
"""
Shallow Copy: A shallow copy creates a new object which stores the reference of the original elements. So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects.
This means, a copy process does not recurse or create copies of nested objects itself.
Deep copy: A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements. The deep copy creates independent copy of original object and all its nested objects.
Both old list and new list are independent.
"""