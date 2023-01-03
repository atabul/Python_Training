#print("Hello World")
a=1
if a>0:
    print("Value of a is greater than 0")

a=5
b=5
print(a+b)

#for comment we use the followint quotes (''') for multiple lines and # for single line
x=5
print(type(x))

a="5"
b="5"
c=a+b
print(type(c))

a=5
b="4"
c=a+b
print(type(c))

#num=10
letter="A"
if letter=="B":
    print("letter is B")
elif letter=="C" or letter=="A":
    print("letter is C")
elif letter=="A":
    print("letter is A")
else:
    print("letter isn't A,B or C") 

#for while
count=0
while(count<3):
    count=count+1
    print("Hello World")


#for
n=4
for i in range(0,n):
    print(i) 

#for Nested Loops type1
for i in range(1,5):
    for j in range(i):
        print(i,end=' ')
        print()

#for nested loops type2
for i in range(1,5):
    for j in range(i):
        print(i,end=' ')
    print()

#for Nested Loops type3
for i in range(1,5):
    for j in range(i):
        print(i,end=' eec ')
    print()

#print(x)

#exception
try:
    print(x)
except:
    print("An exception occurred")

#input function
a=input("Enter first number")
b=input("Enter second number")
c=a+b
print("sum",c)

#input function
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
print("sum",c)

a=input("Enter first name:")
b=input("enter last name:")
print("hello, " + b +" " + a)

