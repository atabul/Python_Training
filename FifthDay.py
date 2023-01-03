#Polymorphism
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old")
    def make_sound(self):
        print("Bark")

cat1=Cat("Kitty",2.5)
dog1=Dog("Rocky",4.8)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


#Incapsulation(Call one function then other can be hidden) and Abstraction(Keep all the function in the different modules)
class Person:
    def __init__(self):
        self.name="Atabul"
    def bio(self):
        self.addr="Bakers Street , London"
        self.taxInfo="HUAPK29971"
        self.contact="01-777-523-342"
        print(self.addr, self.taxInfo, self.contact)
    def interest(self):
        self.favFood="Chinese"
        self.hobbies="Python Programming"
        self.bloodGroup="A+"
        print(self.favFood, self.hobbies, self.bloodGroup)

obj=Person()
print(obj.name)
obj.bio()
obj.interest()



class Library:
    def __init__(self,books):
        self.books=books
    def list_books(self):
        print("Available Books")
        for book in self.books:
            print(book)
    def borrrow_book(self,borrrow_book):
        if borrrow_book in self.books:
            print("Get your book Now")
            self.books.remove(borrrow_book)
        else:
            print("Book not Available")

    def receive_book(self,receive_book):
        print("You returned the Book")
        self.books.append(receive_book)
books=['C','C++','Java']
O=Library(books)

msg="""
1. Display Book 
2. Borrow Book
3. Return Book
"""

while True:
    print(msg)
    ch=int(input("Enter your choice: "))
    if ch==1:
        O.list_books()
    elif ch==2:
        book=input("Enter book name to borrow:")
        O.borrow_book(book)
    elif ch==3:
        book=input("Enter book name to return:")
        O.receive_book(book)
    else:
        print("Thank you come again")
        quite()

      





