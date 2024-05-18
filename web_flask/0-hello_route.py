#!/usr/bin/python3
"""
This script starts a Flask web application listening on 0.0.0.0, port 5000.
It defines a route that displays "Hello HBNB!" when accessed.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def route():
    """Route function for the /airbnb-onepage/ URL."""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
