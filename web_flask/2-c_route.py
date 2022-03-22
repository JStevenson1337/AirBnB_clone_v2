#!/usr/bin/python3
''' Flask entry point '''


from flask import Flask
web_flask = Flask(__name__)


@web_flask.route('/', strict_slashes=False)
def hello():
    ''' hello method '''
    return 'Hello HBNB!'


@web_flask.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' display method '''
    return 'HBNB'


@web_flask.route('/c/<text>', strict_slashes=False)
def display_var(text):
    ''' display variable '''
    return 'C %s' % text.replace("_", " ")


if __name__ == "__main__":
    web_flask.run(host='0.0.0.0', port=5000)