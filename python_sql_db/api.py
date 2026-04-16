import requests , mysql.connector

# EXTRACT

products=requests.get(" https://dummyjson.com/products").json()['products']

print(len(products))

#transer

beauty_products=[]
for p in products:
    if(p['category']=='beauty'):
        beauty_products.append((p["id"],
                                p['title'],
                                p['category'],
                                p['price']))
print(len(beauty_products))
print(beauty_products)

#load into mysql

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
                create table beautyproducts(
                                                pid int,
                                                ptitle varchar(32),
                                                pcategory varchar(32),
                                                price float
                                            )
                '''
    mysql_st='''
                insert into beautyproducts(pid,ptitle,pcategory,price) values(%s,%s,%s,%s);
                    '''
    #dbcursor.execute(sql_st)
    print("Table created successfully")
    dbcursor.executemany(mysql_st,beauty_products)
    print("data inserted into table beautyproducts successfully")
    dbconnection.commit()
except mysql.connector.Error as err:
    print(err)
    
finally:
    if dbconnection:
        dbconnection.close()
    if dbcursor:
        dbcursor.close()



