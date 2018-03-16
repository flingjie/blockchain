# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from bc import init_bc
from bc.wallet import Wallet
from bc.persistence import load_data, save_data


app = Flask(__name__)

bc = init_bc()


@app.route("/")
def index():
    return render_template("index.html", blocks=bc.blocks)


@app.route("/wallets", methods=["GET", "POST"])
def wallets():
    wallet_list = load_data()
    if request.method == "POST":
        wallet = Wallet()
        wallet_list.append(wallet)
        save_data(wallet_list)
    return render_template("wallets.html", wallets=wallet_list)

if __name__ == "__main__":
    app.run(debug=True)
