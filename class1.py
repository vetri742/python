# To create a variable 
Name="String"

# "Everything inside a double quotes is a string"

# print is a function
print(Name)

# Getting input from users
num=int(input("enter num:"))
print(num)

#Control flow statements
for i in range(1,11):
    print(i,"x=",i*2)

#Function 

def name():
    print("This is a function")

#calling a function

name()


#function with return

def player():
    return ("Virat")

print(player())


# function with parameters

def team(name , trophy):
    print(name)
    print(trophy)

#passing arguments

team("virat","Rcb")


#class
class vehicle:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age :", self.age)

s1=vehicle("vetri",22)
s1.display()


# array


multi=[1,2,3,4,6]
multi.append(8)

print(multi)

print(multi[0])
print(len(multi))