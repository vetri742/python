a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

result=a if (a>b and a>c) else(b if b>c else c)

print(result)