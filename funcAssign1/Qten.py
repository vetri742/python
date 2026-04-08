#WRITE A FUNCTION TO SUM ELEMENTS IN A LIST

element=[12,3,55,89]
def sum(n):
    sum=0
    for i in n:
        sum=sum+i
    return sum
print(sum(element))