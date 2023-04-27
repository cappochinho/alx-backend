#!/usr/bin/env python3
"""First attempt at using Babel"""


from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config(object):
    """This class configures available languages in the app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def index():
    """This is the entry point to the app"""

    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Returns the locale from the user's preference"""

    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
