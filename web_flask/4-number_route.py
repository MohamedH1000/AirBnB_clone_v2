#!/usr/bin/python3
"""
a flask web application to be started by this script
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    the hello hbnb to be displayed
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    same but display hbnb
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    display the value of tect after the vriable c
    """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """
    display the value is cool
    that is default after the variable
    python
    """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    display " n is a number"
    if n is integer
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
