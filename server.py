# encoding=utf8  
"""The Markov tweet generator flask app server file."""

from flask import (Flask, jsonify, render_template, request)
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from markov import check_cache, make_markov_tweet

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "752398u5&9563!!hms"


@app.route('/')
def splashpage():
    """Mainpage."""

    return render_template("splashpage.html")


@app.route('/show-markov-tweet')
def send_tweet():
    """Responds to ajax request for a new Markov tweet."""

    tweet_to_send = {}
    twitter_handle = request.args.get("twitter_handle")

    mar_chains = check_cache(twitter_handle)
    tweet_content = make_markov_tweet(mar_chains)

    tweet_to_send['tweet'] = tweet_content

    return jsonify(tweet_to_send)



if __name__ == "__main__":

    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')

