from flask import Flask
import pymongo
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = "My secret key"

#Database
client = pymongo.MongoClient("mongodb+srv://dhruv:dhruv123@cluster0.5pij5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.mobile_meals

from user import routes
from restaurant import routes
from dish import routes
from cart import routes

@app.route('/')
def home():
    return "Home"