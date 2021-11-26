import re
from flask import Flask, request, jsonify
from flask.json import dumps, loads
from app import db
import uuid
from bson.json_util import CANONICAL_JSON_OPTIONS, dumps

class Dish:
    def addNewDish(self):
        dish = {
            "_id": uuid.uuid4().hex,
            "name": request.json['name'],
            "category": request.json['category'],
            "price": request.json['price'],
            "restaurant_id": request.json['restaurant_id'],
            "img_url": request.json.get('img_url', None)
        }
        print(dish)
        try:
            db.dishes.insert_one(dish)
            print("Added")
            return jsonify({"message": "Dish Added", "dish": dish}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Error while adding dish"}), 400 

    def editDish(self, id):
        try:
            db.dishes.update_one({"_id": id},
            {
                "$set" : {
                    "name": request.json['name'],
                    "category": request.json['category'],
                    "price": request.json['price'],
                    "restaurant_id": request.json['restaurant_id'],
                    "img_url": request.json.get('img_url', None)
                }
            })
            return jsonify({"message": "Dish updated"}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Cannot update dish"}), 500  


    def deleteDish(self, id):
        try:
            db.dishes.delete_one({"_id": id})
            return jsonify({"message": "Dish deleted", "id": f"{id}"}),200  
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Cannot delete dish"}), 500   

    def getAllDishes(self, restaurant_id):
        try:
            cursor = db.dishes.find({"restaurant_id": restaurant_id})
            list_dishes = list(cursor)
            return jsonify({"message": "Success", "dishes": list_dishes}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Cannot fetch dishes"}), 500   


    def getSpecificDishes(self):
        dishIds = request.args.getlist('dishId') 
        print(dishIds)
        query = [
             {"$match": {"_id": {"$in": dishIds}}},
             {"$addFields": {"__order": {"$indexOfArray": [dishIds, "$_id" ]}}},
             {"$sort": {"__order": 1}}
            ]
        try:
            dishes = db.dishes.aggregate(query)
            cursor_list = list(dishes)
            return jsonify({"message": "Success", "dishes": loads(dumps(cursor_list))})

        except Exception as ex:
            print(ex)
            return jsonify({"error": "Unable to fetch dishes"})    
