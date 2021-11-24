from flask import Flask, json, request, jsonify
from app import db
import uuid

import cart

# class CartItem:
#      def __init__(self, itemId, quantity):
#         self.itemId = itemId
#         self.quantity = quantity

#      def reprJSON(self):
#         return dict(itemId=self.itemId, quantity=self.quantity)
     

class Cart:
    def addItemToCart(self):
        try:
            # userCart = db.carts.find_one({"_id": userId})
            # items_in_cart = userCart.json.get('items')
            # items_in_cart.append(mealId)
            cartItem = request.json['cart_item']
            db.carts.find_one_and_update(
                {"_id": request.json['_id']},
                {
                    "$push" : {"items": cartItem}
                }, upsert=True
            )
            return jsonify({"message": "Successfully added to cart"}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Error while adding item to cart"}), 400

    def updateCartItem(self):
        try:
            userCart = db.carts.find_one({
                "_id": request.json['_id']
            })

            cart_item = request.json['cart_item']
            print(userCart['items'])
            for index, item in enumerate(userCart['items']):
                if item['itemId'] == cart_item['itemId']:
                    break
                else:
                    index = -1

            if(index != -1):
                userCart['items'][index] = cart_item
                db.carts.find_one_and_update({
                "_id": request.json['_id']},
                {"$set" : {"items": userCart['items']}})

            return jsonify({'message': "Successfully Updated"})

        except Exception as ex:
            print(ex)
            return jsonify({"error": "Error while updating item in cart"}), 400 


    def deleteCartItem(self, userId, itemId):
        try:
            db.carts.update_one({"_id": userId},
            {
                "$pull": {"items": {"itemId": itemId}}
            })
            return jsonify({"message": "Successfully Deleted item"}), 200
        except Exception as ex:
            print(ex)
            return jsonify({"error": "Unable to delete item"}), 400 

    def getUserCart(self, userId):
        try:
            userCart = db.carts.find_one({"_id": userId})
            return jsonify({"message": "Success", "cart": userCart}), 200
        except Exception as ex:
            print(ex) 
            return jsonify({"error": "Unable to get Cart"}), 400                   