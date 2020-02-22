
from flask import Flask, request
import users
import conversations

app = Flask(__name__)
    

@app.route('/user/create/<username>/<group>', methods=['GET']) 
def createUser(username, group):
    return users.createUser(username, group)


@app.route('/chat/create/<chatname>', methods=['GET']) 
def createChat(chatname):
    return conversations.createConversation(chatname)


@app.route('/chat/<chatname>/<username>/<message>', methods=['GET'])
def addMessage(chatname, username, message):
    return conversations.addMessage(chatname, username, message)


@app.route('/chat/adduser/<username>', methods=['GET'])
def addUser(username):
    return users.addUser(username)

app.run("0.0.0.0", 8800, debug=True)