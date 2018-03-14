# -*- coding: utf-8 -*-

from flask import Flask, render_template
from bc import create_bc

app = Flask(__name__)

bc = create_bc()


@app.route("/")
def index():
    return render_template("index.html", blocks=bc.blocks)


if __name__ == "__main__":
    app.run(debug=True)
