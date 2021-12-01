from flask import Flask
from app import app
from order.models import Order

@app.route("/orders/addNewOrder", methods = ["POST"])
def addNewOrder():
    return Order().addNewOrder()

@app.route("/orders/<userId>")
def getUserOrders(userId):
    return Order().getAllOrders(userId)    