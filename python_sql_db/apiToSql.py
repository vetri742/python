import requests , mysql.connector

#EXTRACT

responce=requests.get("https://jsonplaceholder.typicode.com/users")
print(responce)
users=responce.json()
#print(users)

#TRANSFER

users_data=[]
for e in users:
    users_data.append((e['id'],e['email'],e['address']['city']))
print(users_data)

#LOAD TO MYSQL

dbconnection=None
dbcursor=None
 
try:
    dbconnection=mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root",
                                         database="api",
                                         use_pure=True)
    dbcursor=dbconnection.cursor()
    sql_st='''
                insert into userdata(uid,uemail,ucity) values(%s,%s,%s)
            '''
    dbcursor.executemany(sql_st,users_data)
    dbconnection.commit()
    print("inserted data successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    if dbconnection:
        dbconnection.close()
    if dbcursor:
        dbcursor.close()


