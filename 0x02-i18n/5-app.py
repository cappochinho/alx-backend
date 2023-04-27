#!/usr/bin/env python3
"""
Using Flask and Babel to configure a webpage
that renders English and French translations
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    """
    Retrieve user from request
    """

    usr_id = request.args.get('login_as')
    try:
        return users.get(int(usr_id))
    except Exception:
        return None


@app.before_request
def before_request():
    """Before the request"""

    g.user = get_user()


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
