#!/usr/bin/env python3
""" Mock user login """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


def get_user() -> Union[dict, None]:
    """Get user by ID"""
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """Set current user"""
    user = get_user()
    g.user = user


@app.route("/")
def index() -> str:
    """index.html"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
