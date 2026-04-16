import mysql.connector

print('start the program')
dbconnection=None
dbcursor=None

try:
     dbconnection=mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='root',
                                          database='python',
                                          use_pure=True
                                          
                                          )
     print('connection successfull') 
     
     dbcursor=dbconnection.cursor()
     print('connection successfull')
     mysql_st='''
                create table topics(
                topic_id int,
                topic_name varchar(32)
                );

            '''
     dbcursor.execute(mysql_st)
     dbconnection.commit()
     print('Table created successfully')
except Exception as err:
     print(f'failed to connect:{err}')
finally:
    if dbcursor:
        dbcursor.close()
    if dbconnection:
        dbconnection.close()