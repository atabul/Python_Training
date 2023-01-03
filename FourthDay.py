#iterate the given number list of numbers abd print only those numbers which are divisible by 5. Given list is [10,20, 33,46,55]
l=[]
l.append(10)
l.append(20)
l.append(33)
l.append(46)
l.append(55)
myList={x%5 for x in [10,20,33,46,55]}
print(myList)

#Print the following pattern
'''1
   2 2
   3 3 3
   4 4 4 4
   5 5 5 5 5'''

for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()


#write a program to check if the given number is a palindrome number
def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num/10
    if(temp==rev):
        print("The number is palindrome !")
    else:
        print("Not a palindrome!")

num=int(input("Enter a number:"))
palindrome(num)

#Class
class Person:
    def __init__(self, name, age):       #init and str are initialization and structure function and these are standard for all class also take double dash before and after.
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
    def myfunc(self):
        print("The given name is ",self.name)
p1 = Person("Atabul",25)
p2=Person("Raj",23)
print(p1.name)
print(p1.age)
print(p1)
print(p2)
print(p1.myfunc())


class Room:
    length=0.0
    breadth=0.0
    def calculate_area(self):
        print("Area of Room =",self.length*self.breadth)
study_room=Room()
study_room.length=42.5
study_room.breadth=30.8
study_room.calculate_area()

#inheritance
class Animal:
    name=""
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def display(self):
        print("My name is ",self.name)
labrador=Dog()
labrador.name="Atabul"
labrador.eat()
labrador.display()


class Car:
    name=""
    def drive(self):
        print("Drive slow!")
class Hundai(Car):
    def display(self):
        print("The best company in the world",self.name)
abc=Hundai()
abc.name="TVS"
abc.drive()
abc.display()


#Super Method
class Animal:
    name=""
    def eat(self):
        print("i can eat")
class Dog(Animal):
    def eat(self):
        super().eat()       #Call super class using super function
        print("I like to eat bones")
laborador=Dog()
laborador.eat()