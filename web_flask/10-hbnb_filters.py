#!/usr/bin/python3
"""
a flask web application to be started by this script
"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_list_route():
    """
    all cities of a state to be listed
    by this function
    """
    data = {
        "states": storage.all("State").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("10-hbnb_filters.html", models=data)


@app.teardown_appcontext
def close_db(exception=None):
    """
    Sqlalchemy session to be reomoved after each information
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
