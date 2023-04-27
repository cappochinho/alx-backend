#!/usr/bin/env python3
"""Using Flask and Babel to configure a webpage
that renders English and French translations"""

from flask import Flask, g, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    '''
    Config class for flask-babel
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user():
    """Get user from request"""
    user_id = request.args.get('login_as')
    try:
        return users.get(int(user_id))
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request user"""
    g.user = get_user()


@babel.localeselector
def get_local():
    '''Locale selector for Flask-babel'''
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    try:
        user = get_user()
        if user and user['locale'] in Config.LANGUAGES:
            return user['locale']
    except Exception:
        return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    ''' Render index page '''
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
