#!/usr/bin/python3
"""
Implementing a Flask app
"""

from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def home():
    """
    The home function decorated by / and unstrict slashes.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
