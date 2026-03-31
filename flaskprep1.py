def add(*num):

    c=0

    for i in num:
        c+=i
    print(f"sum is {c}")

add(1,3,55,66,2,)


def player(**details):
    for i,j in details.items():
        print(i,j)

player(name="virat", age=37 , status="king", hundreds=85)


def multi(*mul):
    m=1
    for i in mul:
        m *= i
    print(f"the product is {m}")
multi(2,4,6,777,8)





