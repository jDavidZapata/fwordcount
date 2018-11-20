import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

print(os.environ['APP_SETTINGS'])



@app.route('/')
def hello():
    return "Hello World its me DAVE Again changing things Again!!!!"

@app.route('/<name>')
def hello_name(name):
    return "Hello there {}!".format(name)


if __name__ == '__main__':
        app.run()
