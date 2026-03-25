#Create

d={
    "name":"vetri",
    "age":22,
    "skills":["html","css","js","python","mongoDB","SQL"]
}

#Read

print(d)
print(d.get("age"))
print(d["name"])
print(d["skills"])

#Update


d["name"]="virat"
print(d)

#Delete

del d["name"]
print(d)