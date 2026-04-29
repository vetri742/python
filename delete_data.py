
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
            delete from players where pid=%s;
                 
       '''
    value=[(1)]
    

    dbcursor.execute(sql_st,value)
    dbconnection.commit()
    print("deleted successfully")
except mysql.connector.Error as err:
    print(err)
    
finally:
    if(dbconnection):
        dbconnection.close()
    if(dbcursor):
        dbcursor.close()
