#!/usr/bin/env python3
"""Module for basic Flask application"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config:
    """Class for configuration flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Getting and return web page locale"""
    querypara = request.query_string.decode("utf-8").split("&")
    querydict = dict(map(
        lambda k: (k if "=" in k else "{}=".format(k)).split("="),
        querypara
    ))
    if "locale" in querydict:
        if querydict["locale"] in app.config["LANGUAGES"]:
            return querydict["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Home page of Flask application"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
