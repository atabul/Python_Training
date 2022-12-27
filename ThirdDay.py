#Type Conversion
 
# Implicit (Self Change automatic)
'''a=20
b=4.5
print(type(a+b))''' 

'''a=20
b=4.5
c=int(a+b)
print(type(c))'''


#Explicit (Forcefully Change through me) 
'''s="10010"
c=int(s,2)  #Printing string converting to int base 2
print("After converting to integer base 2:",end="")
print(c)'''

'''s="100110"
e=float(s)
print("After converting to float:",end="")
print(e)'''

'''s="100110"
e=float(s)
print("After converting to float:",end="str")
print(e)'''

#List,Tuple, Set and Dictionary

#List
'''l=[]
l.append(5)
l.append(10)
print("Adding 5 to 10 in List",l)
l.pop()
print("popped one element from list",l)
print()'''
 
#Set
'''s=set()
s.add(5)
s.add(8)
print("Adding 5 and 8 in set",s)
s.remove(5)
print("Removing 5 from set ",s)
print()'''

#Tuple
'''l=[]
l.append(5)
l.append(10)
t=tuple(l)
print("Tuple",t)
t.append(5)      #Tuples are imutable, mutable=writable(can be modify) and unmutable=don't writable only readable
print()'''

#Dictionary
'''d={}
d[5]="Five"
d[10]="Ten"
d[10]="Ten"
d[11]="Ten"
#d[11]="Eleven"
print("Dictionary",d)
del d[10]  #remove
print("Dictionary",d)'''

#Examples
#Dictionary
'''myDict={num:num*num for num in range(1,11)}
print(myDict)'''

#List
'''myList={x:x**2 for x in [1,2,3,4,5]}
print(myList)'''

'''newdict={x:x**3 for x in range(10) if x**3%4==0}
print(newdict)

myDict={x:x^2 for x in [1,2,3,4,5]}
print(myDict)'''

'''original_dict={'Jack':38,'Michal':48,'guido':57,'johan':33}
even_dict={k:v for (k,v) in original_dict.items() if v%2==0}
print(even_dict)'''

'''original_dict={'Jack':38,'Michal':48,'guido':57,'Johan':33}
new_dict={k:v for (k,v) in original_dict.items() if v%2!=0 if v<40}
print(new_dict)'''

languages=[
    {"Python":"Machine Lerning","R":"Machine Learning"},
    {"Python":"Web Development","Java Scripit":"Web Development","HTML":"Web Development"},
    {"C++":"Game Development","Python":"Game Development"},
    {"Java":"App Development","Kotlin":"App Development"}
]
#print(*[key for i in languages for key in i.keys()],sep="\n")
#print([key for i in languages for key in i.keys()],sep="\n")
print(*[key for i in languages for key in i.values()],sep="\n")


#Next Class OOP after then Web Development.






