import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.student
student = {
    'id' : '1',
    'name' : 'mike'
}

collection.insert(student)
print(collection.find_one({'name' : 'mike'}))