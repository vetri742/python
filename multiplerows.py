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
                insert into players values(%s,%s,%s)
                '''
    data=[
        (1,'rajat patidhar','batter'),
        (17,'de villiars','batter'),
        (3,'bhuvi','bowler'),
        (11,'hazlewood','bowler')
    ]
    dbcursor.executemany(sql_st,data)
    dbconnection.commit()
    print("Data inserted into table players")
except mysql.connector.Error as err:
    print(err)
    
finally:
    if(dbconnection):
        dbconnection.close()
    if(dbcursor):
        dbcursor.close()
