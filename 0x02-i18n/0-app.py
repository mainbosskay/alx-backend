#!/usr/bin/env python3
"""Moduke for basic Flask application"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index() -> str:
    """Home page of the Flask application"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
