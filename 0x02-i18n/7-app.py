#!/usr/bin/env python3
""" Infer time zone """
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """ App config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """ Get user by ID """
    return users.get(user_id)


@app.before_request
def before_request():
    """ Set current user """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.timezoneselector
def get_timezone():
    """ Get timezone """
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/")
def index():
    """ index.html """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(debug=True)
