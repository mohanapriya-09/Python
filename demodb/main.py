import pymongo
connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection["student_database"]
col = database["Students"]
# col.insert_one({"name": "Mohanapriya", "age": "20", "mobile": 7397671699})
# col.insert_one({"name": "Fida", "age": "20", "mobile": 7334571699})
# col.insert_one({"name": "Pratheepa", "age": "21", "mobile": 7334571699})
# col.insert_many([{"name": "Akshaya", "age": "20", "mobile": 7345456332}, {"name": "Haemi", "age": "20", "mobile": 7333455699},{"name": "Deepthi", "age": "20", "mobile": 7333331699}])
for i in col.find():
    print(i['name'])
print("Successfully saved")
