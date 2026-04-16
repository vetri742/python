import mysql.connector 
print("okay")
try:
    conn=dbconnection=mysql.connector.connect(host='127.0.0.1',
                                          user='root',
                                          password='root',
                                          database='python',
                                          #port=3306,
                                          #auth_plugin='mysql_native_password',
                                          #connection_timeout=10,
                                          use_pure=True
                                          
                                          )
    print('connection successfull') 
except Exception as err:
    print(err)