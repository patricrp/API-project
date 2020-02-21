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
def checkUser(name):
    #Check if user exists
    if db['Users'].count_documents({ 'username': name }, limit = 1) != 0:
        query = db['Users'].find_one({'username': name})
        return dumps(query)
    else:
        return 'Try to create the user'