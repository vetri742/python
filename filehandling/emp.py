import csv
import json


#extract

fp=open("emp.csv","r")
fp1=(csv.reader(fp))
print(fp1)
data=list(fp1)
print(data)
data_csv=data[1:] #excluding the 1st row
print(data_csv)

#transfer

emp_json=[]
for emp in data_csv:
   emp_json.append({"eid":int(emp[0]),"username":emp[1],"gender":emp[2]})
print(emp_json)


#load

data_j=open("emp.json","w")
json.dump(emp_json,data_j)
print("successfull")




