# loads--- convert from json string to python data
#dumbs-- convert from pythoin datA TO json data
import json
emp={"eid":101,"ename":"vetri","availability":True}
print(emp)
employee=json.dumps(emp)
print(employee)