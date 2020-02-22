from pymongo import MongoClient
from bson.json_util import dumps
from errorHandler import jsonErrorHandler

client = MongoClient("mongodb://localhost/Conversations")
db = client.get_database()
        


@jsonErrorHandler
def createUser(name):
    #Check if user exists
    if db['Users'].count_documents({ 'username': name }, limit = 1) != 0:
        return """
    <img src="https://cdn.memegenerator.es/imagenes/memes/full/4/19/4199711.jpg">
    """
    #Create user
    else:
        query = db['Users'].insert({'username': name})
        if not query:
            raise ValueError("User not inserted")
        return {"user_id":str(query)}


@jsonErrorHandler
def addUser(name):
    #Look for user's group:
    grupo = list(df_reduced['Groups'][df_reduced['Characters'] == user])[0]
    #Look for user's id
    i = list(db['Users'].find({'username': user}, {'_id':1}))[0]['_id']
    #Look for group's id
    ig = list(db['Conversations'].find({'Group':grupo}, {'_id':1}))[0]['_id']
    query = list(db['Conversations'].update({"_id":ig}, {'$push': {'Characters': {'username': user, '_id':i}}}))
    return 'User added to the chat'




