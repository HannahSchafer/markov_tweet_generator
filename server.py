# encoding=utf8 
"""The Markov tweet generator flask app server file."""

from flask import (Flask, jsonify, render_template, request, make_response)
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "752398u5&9563!!hms"

@app.route('/')
def splashpage():
    """Mainpage."""

    return render_template("splashpage.html")


@app.route('/get-markove-tweet.json')
def send_tweet():
    """Responds to ajax request for a new Markov tweets."""

    pass














if __name__ == "__main__":

    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')

