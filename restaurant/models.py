from flask import Flask, request, jsonify
from app import db
import uuid

import restaurant

class Restaurant:
    def addNewRestaurant(self):
        restaurant = {
            "_id" : uuid.uuid4().hex,
            "name" : request.json['name'],
            "address": request.json['address'],
            "city": request.json['city'],
            "cuisine": request.json['cuisine'],
            "open_time": request.json['open_time'],
            "close_time": request.json['close_time'],
            "img_url": request.json.get('img_url', None)
        }
        print(restaurant)
        try:
            db.restaurants.insert_one(restaurant)
            print("Added")
            return jsonify({"message": "Restaurant Added", "restaurant": restaurant}), 200
        except Exception as ex:
            print("Exception")
            return jsonify({"error": "Error while adding restaurant"}), 400    

    def editRestaurant(self,id):
        try:
            db.restaurants.update_one({"_id": id},
            {
                "$set" : {
                    "name": request.json['name'],
                    "address": request.json['address'],
                    "city": request.json['city'],
                    "cuisine": request.json['cuisine'],
                    "open_time": request.json['open_time'],
                    "close_time": request.json['close_time'],
                    "img_url": request.json.get('img_url', None)
                }
            })
            return jsonify({"message": "Restaurant updated"}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Cannot update restaurant"}), 500


    def deleteRestaurant(self, id):
        try:
            db.restaurants.delete_one({"_id": id})
            return jsonify({"message": "Restaurant deleted", "id": f"{id}"}),200  
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Cannot delete restaurant"}), 500 

    def getAllRestaurants(self):
        try:
            cursor = db.restaurants.find({})
            list_restaurants = list(cursor)
            return jsonify({"message": "Success", "restaurants": list_restaurants}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Cannot fetch restaurants"}), 500  

    def getSpecificRestaurant(self, restaurantId):
        try:
            restaurant = db.restaurants.find_one({"_id" : restaurantId})
            return jsonify({"message": "Success", "restaurant": restaurant}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error" : "Error fetching restaurant"}), 500        
