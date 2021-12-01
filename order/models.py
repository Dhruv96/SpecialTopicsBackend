from flask import Flask, request, jsonify
from app import db

class Order:
    def addNewOrder(self):
        try:
            order = request.json['order']
            db.orders.find_one_and_update(
                {"_id": request.json['_id']},
                {
                    "$push" : {"order": order}
                }, upsert=True
            )
            return jsonify({"message": "Order Placed Successfully"}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Error while Placing Order"}), 400


    def getAllOrders(self, userId):
        try:
            userOrders = db.orders.find_one({"_id": userId})
            return jsonify({"message": "Success", "orders": userOrders}), 200
        except Exception as ex:
            print(ex) 
            return jsonify({"error": "Unable to get Orders"}), 400    
