#!/usr/bin/python3
"""
a flask web application to be started by this script
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list_to_cities():
    """
    all the states to be listed
    """
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db(exception=None):
    """
    after each request remove session sqlalchemy
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
