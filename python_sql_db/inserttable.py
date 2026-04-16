import mysql.connector
dbconnection=None
dbcursor=None
try:
    dbconnection=mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root",
                                         database="python",
                                         use_pure=True)
    dbcursor=dbconnection.cursor()
    mysql_st='''
                insert into topics(topic_id,topic_name) values(1,"Identifiers");
                '''
    dbcursor.execute(mysql_st)
    dbconnection.commit()
    print("inserted datas successfully")

except mysql.connector.Error as err:
    print(err)
finally:
    if dbconnection:
        dbconnection.close()
    if dbcursor:
        dbcursor.close()