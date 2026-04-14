
try:
    fp=open("data.txt", 'r')
    read=fp.read()
    print(read)
except FileNotFoundError :
    print("File does not exist")

print("GE")


