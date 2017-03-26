from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is a python flask site'