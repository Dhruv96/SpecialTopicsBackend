from flask import Flask
from dish.models import Dish
from app import app


@app.route("/dish/add", methods = ["POST"])
def addDish():
    return Dish().addNewDish()

@app.route("/dish/edit/<id>", methods = ["PUT"])
def editDish(id):
    return Dish().editDish(id)

@app.route("/dish/delete/<id>", methods = ["DELETE"])
def deleteDish(id):
    return Dish().deleteDish(id)   

@app.route("/dish/all/<restaurant_id>")
def getAllDishes(restaurant_id):
    return Dish().getAllDishes(restaurant_id)

@app.route("/dish/getSpecificDishes")
def getSpecificDishes():
    return Dish().getSpecificDishes()    