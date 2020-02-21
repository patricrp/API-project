
from flask import Flask, request
import users

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/createuser/<nameuser>')
def createUser(nameuser):
    return users.createUser(nameuser)
        

app.run("0.0.0.0", 8800, debug=True)