# OOPs concepts:

print("----------------1. built in function-------------------")
x='chinthalapalli'
print("length of chinthalapalli is:",len(x))


print("-------2. Using algorithm i.e, Without functions-------")

x="9494912885"
y=0
for cbr in x :
    y+=1
    print("length of string", y)
'''
print("------------------with functions-----------------")
x="9494917633"
  def find_length(in_str=None):
    y=0
    for z in in_str :
        x+=1
        return x
    print("length of x is :",find_length(x))
'''

print("--------------- Instance Variable-------------------")

class Student:
    def __init__(self,name,id_number,age,mobile):
        self.name=name
        self.id_number=id_number
        self.age=age
        self.mobile=mobile
x=Student("chinthalaplli",1049535,23,9494912885)
print("object1")
print("name:",x.name)
print("id_number:,",x.id_number)
print("student age:",x.age)
print("mobilenumber:",x.mobile)

#create second object
y=Student("basireddy",13910410,22,9494917633)
print("===========second object ==============")
print("name:",y.name)
print("id_number:",y.id_number)
print("student:",y.age)
print("y.mobile:",y.mobile)


# Without oops concepts
  # 1. Retrieve the student data - RETRIEVAL/READ
print("====================with out oops conscept===========================")

Student = int(input("enter the studentid"))
name = input("enter the name")
fee = int(input("enter the feee"))

    # BEHAVIOR
def get_edata(Student, name, fee):
 fee = fee + fee * 10 / 100
 print("student  after fine :", Student, " - ", name, " - ", fee)
get_edata(Student, name, fee)


print("-----With oops concepts--------")
''''
class Student:
    # STATE   # fields
    def __init__(self, id, name, fee):  # parameters
        self.id = id      # RHS --> Local variables
        self.name = name  # LHS --> Instance variables
        self.fee = fee      # self -> instance/object/ref variable

    # BEHAVIOR  # methods
    def get_student_details(self):
        self.fee = self.fee + self.fee*10/100
        print("student information :", self.id, " - ", self.name, " - ", self.sal)


# object creation
chinthalapalli = Student(100, 'chinthalapalli', 10000)
chinthalapalli.get_Student_details()
swetha = Student(101, 'swetha', 15000)
swetha.get_Student_details()

gowtham = Student(102, 'gowtham', 20000)
gowtham.get_student_details()
'''
print("-----------buyer class-----------------")
class Buyer:
    # STATE
    def __init__(self,  name,mobile, price):
        self.mobile = mobile
        self.name = name
        self.price = price

    # BEHAVIOR
    def get_buyer_details(self):
        print("Buyer details : ", self.mobile, self.name, self.price)

moible= int(input("enter the mobile number : "))
name = input("Enter the buyer name : ")
price = int(input("Enter student price : "))

cbr = Buyer( name, price,)
Buyer.get_buyer_details()

chinthalapalli = Buyer( 'cbr', 90090)
chinthalapalli.get_Buyer_details()

print(chinthalapalli, id(chinthalapalli), type(chinthalapalli))
# 10 int 10.5 float "hello" string

# class   n no of objects

print(cbr)
print(chinthalapalli)



