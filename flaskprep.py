def name(player,*args):
    # *args is used to get n number of input from users as tuple
    print(player,args)
name("vetri","batter","leg spin")


def details(**kwargs):
    # **kwars used to get n number of input from users as dictionary
    print(kwargs)

details(name="vetri", age=22,place="vellore")

def n(*args):
    for i in args:
        print(i)
n("vetri","virat","rohit","watson","cook")

def x(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")
x(name="vetri", age=22,place="vellore",degree="MCA")


list=[1,2,3,4,5,6]
print(*list) #unpacks the list
