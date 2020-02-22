from pymongo import MongoClient
from bson.json_util import dumps
from errorHandler import jsonErrorHandler

client = MongoClient("mongodb://localhost/Conversations")
db = client.get_database()
        


@jsonErrorHandler
def createUser(name, group):
    #Check if user exists
    if db['Users'].count_documents({ 'username': name }, limit = 1) != 0:
        return """
    <img src="https://cdn.memegenerator.es/imagenes/memes/full/4/19/4199711.jpg">
    """
    #Create user
    else:
        query = db['Users'].insert({'username': name,'Group': group})
        if not query:
            raise ValueError("User not inserted")
        return {"user_id":str(query)}


@jsonErrorHandler
def addUser(username):
    #Look for user an group ids and add to the conversation
    i = list(list(db['Users'].find({'username': 'Lisa Simpson'}, {'_id':1, 'Group':1}))[0].values())
    ig = list(db['Conversations'].find({'Group':i[1]}, {'_id':1}))[0]['_id']
    query = list(db['Conversations'].update({"_id":ig}, {'$push': {'Characters': {'username': username, '_id':i[0]}}}))
    return 'User added to the chat'




