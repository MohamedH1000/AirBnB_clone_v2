#!/usr/bin/python3
"""
a flask web application to be started by this script
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    list all the states
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id_route(id):
    """
    a state to be represented by the id
    """
    state = None
    for a in storage.all("State").values():
        if a.id == id:
            state = a
            break
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def close_db(exception=None):
    """
    after each request remove session sqlalchemy
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
