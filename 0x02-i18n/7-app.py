#!/usr/bin/env python3
'''Basic flask app for i18n'''


from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import UnknownTimeZoneError, timezone
import pytz


app = Flask(__name__)
babel = Babel(app)

# mock database for task 5
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
    """Before request to stash user"""
    g.user = get_user()

@babel.timezoneselector
def get_timezone():
    ''' get timezone from ULR
        Find timezone parameter in URL parameters
        Find time zone from user settings
    '''
    tz = request.args.get('timezone')
    if tz:
        try:
            timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass
    if g.user:
        user_tz = g.user.get('timezone')
        if user_tz:
            # 2. User settings
            try:
                timezone(user_tz)
                return user_tz
            except UnknownTimeZoneError:
                pass
    return Config.BABEL_DEFAULT_TIMEZONE





@babel.localeselector
def get_local():
    '''Locale selector for flask-babel'''
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
    ''' Return the index page '''
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
