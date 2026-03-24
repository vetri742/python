# control flow statements

# conditional statements

a=int(input("Enter num:"))

if (a%2==0):
    print("even")
else:
    print("odd")

# with elif 

maths_mark=int(input("Enter maths mark:"))
computer_mark=int(input("Enter computer mark:"))

if(maths_mark>computer_mark):
    print("Maths mark is greater than computer mark")
elif(computer_mark==maths_mark):
    print("Equal marks in both the subj")

elif(maths_mark<computer_mark):
    print("computer mark is greater than maths mark")
else:
    print("Enter valid marks")

# Iterative statements

for i in range(5):
    print("vetri")

count=0
while(count<5):
    print("virat")
    count+=1
