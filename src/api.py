
from flask import Flask, request
import users
import conversations
import sentiment

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


@app.route('/chat/<chatname>/list', methods=['GET'])
def getChat(chatname):
    return conversations.getChat(chatname)

@app.route('/chat/<chatname>/userlist', methods=['GET'])
def getListChat(chatname):
    return conversations.getListChat(chatname)

@app.route('/chat/<chatname>/sentiment', methods=['GET'])
def sentimentChat(chatname):
    return sentiment.sentimentText(chatname)

app.run("0.0.0.0", 8800, debug=True)