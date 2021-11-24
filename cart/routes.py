from flask import Flask
from app import app
from cart.models import Cart


@app.route("/cart/addItem", methods=['POST'])
def addItemToCart():
    return Cart().addItemToCart()

@app.route("/cart/updateItem", methods = ["PUT"])
def updateItemInCart():
    return Cart().updateCartItem()

@app.route("/cart/deleteItem", methods = ["DELETE"])    
def deleteItemInCart():
    return Cart().deleteCartItem()  

@app.route("/cart/userCart")
def getUserCart():
    return Cart().getUserCart()      