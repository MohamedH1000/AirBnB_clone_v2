#!/usr/bin/python3
"""
a flask web application to be started by this script
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    list all the states
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db(exception=None):
    """
    remove sqlalchemy session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
