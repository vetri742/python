import json

data=open("exp.json","r")
fp=open("one.json","w")
data2=json.load(data)
json.dump(data2,fp)
