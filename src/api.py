
from flask import Flask, request
import users

app = Flask(__name__)
    

@app.route('/user/create/<username>', methods=['GET']) 
def createUser(username):
    return users.createUser(username)
        
@app.route('/user/check/<username>', methods=['GET']) 
def checkUser(username):
    return users.checkUser(username)


@app.route('/chat/create', methods=['GET'])
def createConversation(*args):
    return users.createConversation(*args)


app.run("0.0.0.0", 8800, debug=True)