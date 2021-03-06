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
    users = list(db['Conversations'].distinct('Characters'))
    if db['Conversations'].count_documents({'Group':chatname}, limit = 1) != 0:
        for user in users:
            if username == user['username']:
                i = list(db['Conversations'].find({'Group':chatname}, {'_id':1}))[0]['_id']
                query = list(db['Conversations'].update({"_id":i},{"$push":{"Message": {'username': username, 'message': message}}}))
                return 'Great. Included'
            else:
                ValueError("User not in the group")
    else:
        ValueError("Dialogue not added")

@jsonErrorHandler 
def getChat(chatname):
    # Get a json array of users and messages
    query = list(db['Conversations'].find({'Group':chatname}))[0]['Message']
    return dumps(query)


@jsonErrorHandler 
def getListChat(chatname):
    # Get an array of messages
    query = list(db['Conversations'].find({'Group':chatname}))[0]['Message']
    conversation = []
    for q in query:
        conversation.append(q)
    messages = []
    for message in conversation:
        messages.append(message['message'])
    return dumps(messages)