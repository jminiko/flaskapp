from flask import Flask
from
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/saveimage', methods=['POST']))
def runnodet():

if __name__ == '__main__':
    app.run()
