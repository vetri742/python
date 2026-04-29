import pymongo,requests
response=requests.get("https://jsonplaceholder.typicode.com/users")
users=response.json()
#insert data into mongodb collection employees
try:
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client["6pm"]
   employee_collection=db["employees"]
   employee_collection.insert_many(users)
   print("data inserted sucessfully")
except Exception as error:
   print(error)