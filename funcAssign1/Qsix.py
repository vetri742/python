
#WRITE A FUNTION TO CALCULATE THE FACTORIAL OF A NUMBER

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n* factorial(n-1)
print(factorial(5))