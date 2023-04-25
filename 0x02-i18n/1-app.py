#!/usr/bin/env python3
"""First attempt at using Babel"""


from flask import Flask, render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
babel = Babel(app)


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

app.config.from_object(Config)


@app.route("/")
def index():
    """This is the entry point to the app"""

    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
