from flask import Flask
import pymongo
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = "My secret key"

#Database
client = pymongo.MongoClient("mongodb+srv://dhruv:dhruv123@cluster0.5pij5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.mobile_meals

from user.routes import *
from restaurant.routes import *
from dish.routes import *
from cart.routes import *
from order.routes import *
from ratings.routes import *

# @app.route('/')
# def home():
#     return "Home"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
