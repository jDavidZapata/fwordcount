import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello World its me Again and Again!!!!"

@app.route('/<name>')
def hello_name(name):
    return "Hello there {}!".format(name)


if __name__ == '__main__':
        app.run()
