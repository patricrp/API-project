
from flask import Flask, request
import users

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/createcollection/<name>', methods=['GET'])
def createCollection(name):
    return users.createCollection(name)

    

@app.route('/user/create/<username>', methods=['GET']) 
def createUser(username):
    return users.createUser(username)
        
@app.route('/checkuser/<username>', methods=['GET']) 
def checkUser(username):
    return users.checkUser(username)


app.run("0.0.0.0", 8800, debug=True)