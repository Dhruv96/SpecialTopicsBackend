from flask import Flask, json, request, jsonify
from app import db

     

class Cart:
    # function to add items in cart
    def addItemToCart(self):
        try:
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

    # function to  update cart items
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

    # function to delete cart item from specific user's cart
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

    # Function that returns user's cart
    def getUserCart(self, userId):
        try:
            userCart = db.carts.find_one({"_id": userId})
            return jsonify({"message": "Success", "cart": userCart}), 200
        except Exception as ex:
            print(ex) 
            return jsonify({"error": "Unable to get Cart"}), 400 

    # function to clear user cart once order is placed
    def clearCart(self, userId):
        try:
            db.carts.delete_one({"_id": userId})
            return jsonify({"message": "Successfully Cleared Cart"}), 200   

        except Exception as ex:
            print(ex)
            return jsonify({"error": "Unable to clear Cart"}), 400                           