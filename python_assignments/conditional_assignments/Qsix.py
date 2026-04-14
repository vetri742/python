# WRITE A PROGRAM TO TAKE A SINGLE DIGIT NUMBER AS A INPUT FROM THE USER AND PRINT IT IN ENGLISH

a=int(input("enter number (0-9):"))
if(a==0):
    print("zero")
elif(a==1):
    print("one")
elif(a==2):
    print("two")
elif(a==3):
    print("three")
elif(a==4):
    print("four")

elif(a==5):
    print("five")

elif(a==6):
    print("six")
elif(a==7):
    print("seven")
elif(a==8):
    print("eight")
elif(a==9):
    print("nine")
else:
    print("enter number between 0-9")


# ANOTHER WAY USING LIST

words=["zero","one","two","three","four","five","six","seven","eight","nine"]

number=int(input("enter num:"))

if(0<=number<=9):
    print(words[number])
else:
    print("Enter number between 0-9")
