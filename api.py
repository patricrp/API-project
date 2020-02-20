
#!/bin/bash

from flask import Flask, request
from tas import queryTas, tas

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'


app.run("0.0.0.0", 8800, debug=True)