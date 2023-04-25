#!/usr/bin/env python3
"""This app is a basic flask app"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """This is the entry point to the app"""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
