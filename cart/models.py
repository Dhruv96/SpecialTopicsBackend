from flask import Flask, json, request, jsonify
from app import db
import uuid

import cart

class CartItem:
     def __init__(self, itemId, quantity):
        self.itemId = itemId
        self.quantity = quantity

     def reprJSON(self):
        return dict(itemId=self.itemId, quantity=self.quantity)
     

class Cart:
    def addItemToCart(self):
        try:
            # userCart = db.carts.find_one({"_id": userId})
            # items_in_cart = userCart.json.get('items')
            # items_in_cart.append(mealId)
            cartItem = CartItem(request.json.get('itemId'), request.json.get('quantity'))
            db.carts.find_one_and_update(
                {"_id": request.json['_id']},
                {
                    #"$set" : {"userId": request.json['userId']},
                    "$push" : {"items": cartItem.reprJSON()}
                }, upsert=True
            )
            return jsonify({"message": "Successfully added to cart"}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Error while adding item to cart"}), 400

