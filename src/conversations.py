from pymongo import MongoClient
from bson.json_util import dumps
from errorHandler import jsonErrorHandler

client = MongoClient("mongodb://localhost/Conversations")
db = client.get_database()



@jsonErrorHandler
def createConversation(*args):
    query = db['Conversations'].insert_one(
        {
            'Characters': [args]
        }

    )
    return dumbs(query)

    '''



    for index, value in df.iterrows():
         query = db['Conversations'].insert({
            'Character': args,
            'Message': content,
            'Chat': casa
            'user_i': db['Users'].find({'name':name}, {'_id':1})
        }
         )

'''