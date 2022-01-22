print("1.=================find the length of string===============================")
#Using the built-in function len. The built-in function len returns the number of items in a container.

str="chinthalaplli"
print("length of string is ::",len(str))

print("===========2.find the length of string using algorithm============")
x=input("enter the string")
le =0
for char in x :
 le+= 1
 print("lengthe of sting is ::",le)




print("============find the length of string using functions==========")
# Python code to demonstrate string length
# using join and count

# Returns length of string
def findLen(str):
	if not str:
		return 0
	else:
		some_random_str = "chinthalaplli"
		return ((some_random_str).join(str)).count(some_random_str) + 1

str = "vn2solutions"
print(findLen(str))

print("===========String slicing ================")
# Python program to demonstrate
# string slicing


# Using indexing sequence
# Python program to demonstrate
# string slicing

# String slicing
String ='CHINTHALPALLI BASIREDDY'

# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])


print("=====================Swapping Characters in a Python String================")
# Swapping Characters in a Python String

x = "Computer"

print("============   INHERRITANCE  ==================")
class ParentClass:
    string = input("enter the string ::")

    def display(self):
        return self.string

class ChildClass(ParentClass):
    pass

child = ChildClass()

print(child.display())

print("================= second example inherritance=====================")
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Professor(Person):

    def isProfessor(self):
        return f"{self.name} is a Professor"

sir = Professor("narasimha", 30)

print(sir.isProfessor())