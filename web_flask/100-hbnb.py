#!/usr/bin/python3
"""
start a flask web application by this script
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def states_list_route():
    """
    all cities of a state to be listed
    """
    data = {
        "states": storage.all("State").values(),
        "places": storage.all("Place").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("100-hbnb.html", models=data)


@app.teardown_appcontext
def close_db(exception=None):
    """
    remove the current sqlalcehmy session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
