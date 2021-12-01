from flask import Flask
from app import app
from restaurant.models import Restaurant

@app.route("/restaurant/add", methods = ["POST"])
def addRestaurant():
    return Restaurant().addNewRestaurant()

@app.route("/restaurant/edit/<id>", methods = ["PUT"])
def editRestaurant(id):
    return Restaurant().editRestaurant(id)    

@app.route("/restaurant/delete/<id>", methods = ["DELETE"])
def deleteRestaurant(id):
    return Restaurant().deleteRestaurant(id)   

@app.route("/restaurant/all")
def getAllRestaurants():
    return Restaurant().getAllRestaurants() 

@app.route("/restaurant/<restaurantId>") 
def getSpecificRestaurant(restaurantId):
    return Restaurant().getSpecificRestaurant(restaurantId)   