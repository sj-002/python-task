import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = [
    {'_id': 1, 'name': 'John','address': 'Highway37'},
{'_id': 2, 'name': 'Peter','address': 'Lowstreet 27'},
{'_id': 3, 'name': 'Amy','address': 'Apple st 652'},
{'_id': 4,'name': 'Hannah','address': 'Mountain 21'},
{'_id': 5,'name': 'Michael','address': 'Valley 345'},
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'},
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'},
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'},
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'},
{'_id': 10, 'name': 'Vicky','address': 'Yellow Garden 2'},
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'},
{'_id': 12,'name': 'William', 'address': 'Central st 954'},
{'_id': 13, 'name': 'Chuck','address': 'Main Road 989'},
{'_id': 14, 'name': 'Viola','address': 'Sideway 1633'}
]

        #insert method
# x = mycol.insert_many(mydict)

        #find method
x = mycol.find_one()
for x in mycol.find():
    print(x)

        #query method
# myquery = { "address": "Park Lane 38" }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#     print(x)

        #update method
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)
# for x in mycol.find():
#   print(x)