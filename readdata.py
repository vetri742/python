
import mysql.connector 
dbconnection=None
dbcursor=None
try:
    dbconnection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='rcb'
    )
    dbcursor=dbconnection.cursor()
    sql_st='''
            select*from players;     
       '''
    

    dbcursor.execute(sql_st)
    employees=dbcursor.fetchall()
    for e in employees:
        print(e)
except mysql.connector.Error as err:
    print(err)
    
finally:
    if(dbconnection):
        dbconnection.close()
    if(dbcursor):
        dbcursor.close()
