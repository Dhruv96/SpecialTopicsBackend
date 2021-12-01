from flask import Flask
from app import app
from cart.models import Cart


@app.route("/cart/addItem", methods=['POST'])
def addItemToCart():
    return Cart().addItemToCart()

@app.route("/cart/updateItem", methods = ["PUT"])
def updateItemInCart():
    return Cart().updateCartItem()

@app.route("/cart/deleteItem/<userId>/<itemId>", methods = ["DELETE"])    
def deleteItemInCart(userId, itemId):
    return Cart().deleteCartItem(userId, itemId)  

@app.route("/cart/userCart/<userId>")
def getUserCart(userId):
    return Cart().getUserCart(userId)  

@app.route("/cart/clearCart/<userId>", methods = ["DELETE"])
def clearCart(userId):
    return Cart().clearCart(userId)        