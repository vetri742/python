def outer():
    print("outer")
    def inner():
        print("inner")
    return inner
outer()()

def calculate():
    print("results")
    def add(a,b):
        print(a+b)
    def sub(a,b):
        print(a-b)
    def mul(a,b):
        print(a*b)
    def div(a,b):
        print(a/b)
    return add,sub,mul,div
x=calculate()
x[1](3,5)
x[0](2,5)
x[3](4,8)
x[3](33,77)