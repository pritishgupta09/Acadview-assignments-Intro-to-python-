#Q.1 Create a list with user defined inputs.

n=int(input("Enter the number of elements in the list: "))
a=[]
for i in range(0,n):
    b=input("Enter the values in the list: ")
    a.append(b)
print(a)

#Q.2 Add ['google','apple',''facebook','microsoft','tesla'] to above created list

a.append('google')
a.append('apple')
a.append('facebook')
a.append('microsoft')
a.append('tesla')
print(a)

#Q.3 Count the number of time an object occurs in a list.

c=input("Enter the object: ")
print(a.count(c))

#Q.4 Create a list with numbers and sort it in ascending order.

list2=[9,54,15,87,525,98,1]
list2.sort()
print(list2)

#Q.5 Merge two 1-d arrays A and B into single array C in ascending order.

a=[2,6,4]
b=[5,3,1]
c=a+b
c.sort()
print(c)

#Q.6 Count even and odd numbers in the list

list=[24,15,21,34,89,75,38]
even=0
odd=0
for i in list:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("No. of even elements are: ",even)
print("No. of odd elements are: ",odd)

#Tuples

#Q.7 Reverse a tuple in python

tuple=(1,2,3,4,5)
print(tuple[::-1])

#Q.8 To find largest and smallest element of tuple

tuple1=(10,20,50,30,150,119,520)
print("Max value of tuple is: ",max(tuple1))
print("Min value of tuple is: ",min(tuple1))

#Strings

#Q.9 Convert string into uppercase

str=input("Enter any string in lowercase: ")
print("Uppercase: ",str.upper())

#Q.10  Print true if string contains all numeric characters

str1=input("Enter string: ")
print(str1.isdigit())

#Q.11 Replace the word "World" with your name in the string "Hello World"

string = "Hello World"
print(string.replace('World','Pritish'))