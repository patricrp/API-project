from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient("mongodb://localhost/Conversations")
db = client.get_database()


'''
def createColUsers(name):
    #Check if exists
    collection = db.list_collection_names()
    if name in collection:
        return 'The collection exists'
    else:
        #Create collection
        return db.createCollection(f'{name}')
'''

@jsonErrorHandler
def createUser(name):
    #Check if user exists
    if db['Users'].count_documents({ 'username': name }, limit = 1) != 0:
        return 'Username already exists'
    #Create user
    else:
        db['Users'].insert_one({'username': name})
        query = db['Users'].find_one({'username': name})
        print(query)
        if not query:
            raise ValueError("User not inserted")
        return dumps(query)