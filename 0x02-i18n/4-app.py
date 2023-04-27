#!/usr/bin/env python3
"""
Using Flask and Babel to configure a webpage
that renders English and French translations
"""


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


@app.route("/", methods=['GET'])
def index():
    """This is the entry point to the app"""

    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Returns the locale from the user's preference
    Allows a user to pass a preferred translation of
    a webpage as a query string
    """

    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
