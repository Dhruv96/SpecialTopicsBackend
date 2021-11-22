from flask import Flask
from app import app
from cart.models import Cart


@app.route("/cart/addItem", methods=['POST'])
def addItemToCart():
    return Cart().addItemToCart()