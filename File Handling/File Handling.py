#Q.1)Write a Python program to read n lines of a file

n=int(input("Enter a number: "))
a=open('Text File 1.txt','r')
for i in range(0,n):
    value=a.readline()
    print(value)
a.close()

#Q.2)Write a Python program to count the frequency of words in a file.

f=open('Text File 1.txt','r')
a=f.read()
n=input("Enter word to check frequency: ")
b=a.count(n)
print("{} occurs {} times ".format(n,b))

#Q.3)Write a Python program to copy the contents of a file to another file

f1=open('Text File 2.txt','r')
a=f1.read()
f1.close()
print("Before copying")
f2=open('Text File 3.txt','r')
b=f2.read()
print(b,"\n")
print("After copying","\n")
f2.close()
f2=open('Text File 3.txt','a')
f2.write(a)
f2.close()
f2=open('Text File 3.txt','r')
c=f2.read()
print(c)
f2.close()

#Q.4)Write a Python program to combine each line from first file with the corresponding line in second file.

a=open('Text File 1.txt','r')
b=open('Text File 2.txt','r')
c=open('Text File 3.txt','w+')
x=a.readlines()
y=b.readlines()
for i,j in zip(x,y):
    c.write(i)
    c.write(j)
c.close()
c=open('Text File 3.txt','r')
f=c.read()
print(f)
c.close()
b.close()
a.close()

#Q.5)Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

list=[]
f2=open('Text File 5.txt','w+')
for i in range(0,10):
    num=int(input("Enter a value"))
    list.append(num)
f1=open('Text File 4.txt','a')
f1.write(str(list))
print(list)
list.sort()
f2.write(str(list))
f2.close()
f2=open('Text File 5.txt','r')
b=f2.read()
print(b)
f1.close()
f2.close()