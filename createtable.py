import mysql.connector

dbconnection=None
dbcursor=None

try:
    dbconnection=mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='rcb')
    dbcursor=dbconnection.cursor()
    sql_st='''
                create table players(
                    pid int primary key,
                    pname varchar(32) not null,
                    prole varchar(32) 
                    );
                '''
    dbcursor.execute(sql_st)
    dbconnection.commit()
    print("table created successfully")
except mysql.connector.Error as err:
    print(err)
    
finally:
    if(dbconnection):
        dbconnection.close()
    if(dbcursor):
        dbcursor.close()