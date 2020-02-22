from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from errorHandler import jsonErrorHandler

client = MongoClient("mongodb://localhost/Conversations")
db = client.get_database()



@jsonErrorHandler
def createConversation(chatname):
    if db['Conversations'].count_documents({ 'Group': chatname }, limit = 1) != 0:
        return 'Chat already exists'
    else:
        query = db['Conversations'].insert(
        {
            'Group': chatname,
            'Characters': [],
            'Message': []
        }

        )
        return {"Group":str(chatname)}


@jsonErrorHandler  
def addMessage(chatname, username, message):
    if db['Conversations'].count_documents({'Group':chatname}, limit = 1) != 0:
        i = list(db['Conversations'].find({'Group':chatname}, {'_id':1}))[0]['_id']
        query = list(db['Conversations'].update({"_id":i},{"$push":{"Message": {'username': username, 'message': message}}}))
        return 'Great. Included'
    else:
        raise ValueError("Dialogue not added")
