from flask import Flask, json, request, jsonify
from app import db
import uuid
from flask.json import dumps, loads

class UserRating:
    def addNewRating(self):
        userRating  = {
            "_id": uuid.uuid4().hex,
            "userId" : request.json.get('userId'),
            "rating": request.json.get("rating"),
            "feedback": request.json.get("feedback"),
            "restaurantId": request.json.get("restaurantId")
        } 

        if(db.ratings.insert_one(userRating)):
            return jsonify({"message": "Rating Added"})
        else:
            return jsonify({"error": "Error while adding rating"}), 500   


    def getRestaurantRating(self,restaurantId):
        restaurant_ratings = db.ratings.find({"restaurantId": restaurantId})
        ratingList = list(restaurant_ratings)
        if(restaurant_ratings):
            return jsonify({"message": "Success", "ratings": loads(dumps(ratingList))})
        else:
            return jsonify({"error": "Unable to find rating"}), 500     
    