from flask import Flask
from ratings.models import UserRating
from app import app

@app.route("/restaurants/ratings/addNewRating", methods=['POST'])
def addNewRating():
    return UserRating().addNewRating()

@app.route("/restaurants/ratings/<restaurantId>")
def getRestaurantRatings(restaurantId):
    return UserRating().getRestaurantRating(restaurantId)

