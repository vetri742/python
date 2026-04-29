import pymongo

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['rcb']
    db_collection=db['players']
    db_collection.insert_many([{"pid":17,"pname":"de villiars"},{"pid":333,"pname":"gayle"}])
    print("Multiple documents inserted successfully")
except Exception as err:
    print(err)