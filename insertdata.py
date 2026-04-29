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
                insert into players(pid,pname,prole) values(18,'virat','batter');
                '''
    dbcursor.execute(sql_st)
    dbconnection.commit()
    print("Data inserted into table players")
except mysql.connector.Error as err:
    print(err)
    
finally:
    if(dbconnection):
        dbconnection.close()
    if(dbcursor):
        dbcursor.close()
