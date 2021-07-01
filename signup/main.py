import pymongo
connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection["signdb"]
coll = database['person']
# coll.insert_one({"email": "mohanapriya@gmail.com","user": "Mohanapriya", "mobile": 3456789023, "dob": "09/03/2001"})
# coll.insert_one({"email": "fida@gmail.com","user": "Fida", "mobile": 9426789023, "dob": "27/10/2000"})
email_id = str(input("Enter your emailId"))
for i in coll.find():
    if email_id == i["email"]:
        print("Entered Email Id already existed")
        break
else:
    user_name = str(input("Enter User Name:"))
    mobile_no = int(input("Enter your mobile no:"))
    d_o_b = str(input("Enter your date of birth(dd/mm/yy:)"))
    coll.insert_one({"email": email_id, "user": user_name, "mobile": mobile_no, "dob": d_o_b})



print("Successfully")