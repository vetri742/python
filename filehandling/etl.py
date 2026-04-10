import json
import csv

#extract

data=open("exp.json","r")
data_j=json.load(data)
print(type(data_j))

#transfer

data_json=[]

for emp in data_j:
    data_json.append([emp["eid"],emp["name"],emp["gender"]])

print(data_json)


#load

data_csv=open("data.csv","w",newline="")
csv_writer=csv.writer(data_csv)
csv_writer.writerow(['eid','ename','gender'])
csv_writer.writerows(data_json)
print("successfull")