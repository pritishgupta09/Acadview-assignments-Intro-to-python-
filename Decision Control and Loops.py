#Q.1)Take an input from user and decide whether it is a leap year or not.

n=int(input("Enter the year: "))
if(n%4==0 and n%400==0 or n%100!=0):
    print("It is a leap year.")
elif(n%4!=0 and n%100==0 or n%400!=0):
    print("It is not a leap year.")

#Q.2) Take length and breadth from user and check whether the dimensions are of rectangle or square

l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
if(l==b):
    print("It is a square.")
elif(l!=b):
    print("It is a rectangle")

#Q.3)Take the input age of 3 people and determine which is oldest and youngest.

a=int(input("Enter age of A: "))
b=int(input("Enter age of B: "))
c=int(input("Enter age of C: "))
list=[]
list.append(a)
list.append(b)
list.append(c)
for i in list:
    if (a > b and a > c):
        print("A is the oldest.")
    elif (b > a and b > c):
        print("B is the oldest.")
    elif (c > a and c > b):
        print("C is the oldest.")
    if (a < b and a < c):
        print("A is the youngest.")
    elif (b < a and b < c):
        print("B is the youngest.")
    elif (c < a and c < b):
        print("C is the youngest.")
    break

"""
Q.4)Ask a user to enter age,sex(M or F),marital status(Y or N) and then using following rules print their place of service-
1. if employee is female, then she will work only in urban areas.
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
4. And any other input of age should print "ERROR".
"""
age=int(input("Age: "))
sex=input("Sex(M or F): ")
mar=input("Marital Status(Y or N): ")
if(sex=='F' or sex=='f'):
    print("She will work only in urban areas.")
elif(sex=='M' or sex=='m'):
    if(age>=20 and age<=40):
        print("He can work anywhere.")
    elif(age>40 and age<=60):
        print("He will work in urban areas only.")
    else:
        print("ERROR")

"""
Q.5)A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.
"""

q=int(input("Enter quantity: "))
cost=q*100
print("Your billing price is: ",cost)
if(cost>1000):
    print("Congratulations,You get 10% discount.")
    discount=(cost * 10) / 100
    print("You get a discount of: ",discount)
    total=cost-discount
    print("Your total bill is: ",total)
else:
    print("You didn't get any discount.")
    print("Your bill is: ",cost)

#LOOPS

#Q.6)Take 10 integers from user and print it on screen.

list=[]
for i in range(0,10):
    n=int(input("Enter the number: "))
    list.append(n)
print("Numbers entered by the user are: ",list)

"""
Q.7)Write an infinite loop. An infinite loop never ends. Condition is always true.
An infinite loop never ends if condition is always true.
Infinite loop example-
while(0<1):
    print("Infinite loop"). Now loop will continue for infinite number of times as condition is always true.
"""

"""
Q.8)Create a list of integer elements by user input.
Make a new list which will store square of elements of previous list.
"""
n=int(input("Enter the size of the list: "))
list1=[]
list2=[]
for i in range(0,n):
    a=int(input("Enter the elements: "))
    list1.append(a)
print("List 1 is: ",list1)
for i in list1:
    x=i**2
    list2.append(x)
print("List 2 is: ",list2)

#Q.9)From a list containing ints, strings and floats, make three lists to store them separately
list3=[1,'Hello','World',1.5,2.5,2,'Pritish']
x=[]
y=[]
fl=[]
print("List is: ",list3)
for i in list3:
    if isinstance(i,int):
        x.append(i)
    elif isinstance(i,str):
        y.append(i)
    elif isinstance(i,float):
        fl.append(i)
print("Integer list is: ",x)
print("Strings list is: ",y)
print("Float list is: ",fl)

#Q.10) Using range(1,101), make a list containing only prime numbers.

list=[]
for n in range(1,101):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            list.append(n)
print("Prime numbers from 1-101 are: ",list)

"""
Q.11)Print the following patterns:
*
**
***
****
"""
for i in range(1,5):
    print(i*"*")

"""
Q.12)Take inputs from user to make a list.
Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
"""
n=int(input("Enter the size of the list: "))
list=[]
for i in range(0,n):
    a=int(input('Enter elements in list: '))
    list.append(a)
print("List is: ",list)
d=int(input("Enter number you want to delete: "))
for i in list:
    if(i==d):
        list.remove(i)
print(list)