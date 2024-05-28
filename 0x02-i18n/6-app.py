#!/usr/bin/env python3
""" User locale """
from flask import Flask, render_template, request, g
from flask_babel import Babel


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


@babel.localeselector
def get_locale():
    """ Get locale """
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    request_locale = request.headers.get('Accept-Language')
    if request_locale:
        for lang in app.config['LANGUAGES']:
            if lang in request_locale:
                return lang

    return app.config['BABEL_DEFAULT_LOCALE']


@app.route("/")
def index():
    """ index.html """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
