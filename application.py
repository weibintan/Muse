from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is a python flask site'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)