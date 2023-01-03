for i in range(0,10):
    a=i
    print(numbers[i] + numbers[i - 1], end=", ")

    print(i)
    for j in range(1,10):
        b=j
    print(a+b)

    #b=PreviousNo'''

for a in range(0,10):
    CurrentNo=a
    print(a)
    for b in range(1,10):
        PreviousNo=b
        print(b)
        sum=CurrentNo+PreviousNo
    print(sum)


#previous and current no sum
print("Printing current abd previous number and their sum in a range(10")
previous_num=0
for i in range(1,11):
    x_sum=previous_num+1
    print("current_number","previous_num",previous_num,"sum:")
    previous_num=1


def greetings():
    print("Hello World!")
greetings()
print("Printing outside of the function")

def add_numbers(num1,num2):
    sum=num1+num2
    print('Sum: ',sum)
add_numbers(2,4)


def find_square(num):
    result=num*num
    return result
square=find_square(3)
print('Square:',square) 


def square(no):
    x=no*no
    return x
ab=square(6)
print('Square:',ab)


#List Start
def get_square(num):
    return num*num
for i in [1,2,3]:
    result=get_square(i)
    print('Square of ',i,'=',result)

def get_square(num):
    try:
        print(num*num)
    except:
        print("Error")

for i in [1,"Atabul",3]:
    result=get_square(i)
    print('Square of','i','=',result)


#unlnown numbers
def find_sum(*numbers):
    result=0
    for num in numbers:
        result=result+num
    print("Sum=",result)
find_sum(1,2,3)
find_sum(4,9) 


#unknown fruits Awargs
def my_function(*fruits):
    print("The selected fruit is " + fruits[1])
my_function("Apple","Orange","Mango")


#unknown data for key and value in the list of kwargs, (Dictionary)
def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
        #print(key,"is",value.format(key,value))
intro(Firstname="Atabul",Lastname="Nadaf",Age=25,Phone=9812158306)
#intro(Email="djdsj",Country="shf")