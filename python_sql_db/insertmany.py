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
                insert into topics(topic_id,topic_name) values(%s,%s);
                '''
    emp_data=[(2,"operators"),(3,"controlflow"),(4,"functions"),(5,"modules"),(6,"datastructures")]
    dbcursor.executemany(mysql_st,emp_data)
    dbconnection.commit()
    print("inserted many  datas successfully")

except mysql.connector.Error as err:
    print(err)
finally:
    if dbconnection:
        dbconnection.close()
    if dbcursor:
        dbcursor.close()