from flask import Flask, jsonify, request, session
from passlib.hash import pbkdf2_sha256 
import uuid
from app import db
class User:
    # Function that stores user in session object and return logged in user object
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    # Function to sign out user and clear session
    def signout(self):
        if(session.get('logged_in')):
            session.clear()
        return jsonify({"message": "Successfully signed out"}), 200    

    # Function to signup a user
    def signup(self):
        print(request.json)
        #create user
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.json.get('name'),
            "email": request.json.get('email'),
            "password": request.json.get('password'), 
            "address": request.json.get('address'),
            "city": request.json.get('city')
        }
        #encrypt user password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if(db.users.find_one({"email": user['email']})):
            return jsonify({"error": "Email address already in use"}), 400
        if(db.users.insert_one(user)):
            return self.start_session(user)
        return jsonify({"error": "Signup Failed"}), 400   

    # Function to login user
    def login(self):
        user = db.users.find_one({
            "email": request.json.get('email')
        })  

        # Comparing password by encrypting password entered by user with stored encrrypted password
        if user and pbkdf2_sha256.verify(request.json.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({"error": "Invalid Login Credentials"}), 401  

    # Function to update user profile
    def updateProfile(self):
        user = {
            "_id": request.json.get("_id"),
            "name": request.json.get('name'),
            "email": request.json.get('email'),
            "password": request.json.get('password'), 
            "address": request.json.get('address'),
            "city": request.json.get('city')
        }
    
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        try :
            db.users.find_one_and_update({"_id": user['_id'] },
            {"$set" :  {"name" : user['name'],
            "email" : user['email'],
            "password" : user['password'],
            "address": user['address'],
            "city" : user['city']}})

            del user['password']
            print(user)
            return jsonify({"message" : "Success", "user" : user})

        except Exception as ex:
            print(ex) 
            return jsonify({"error": "Unable to update user"}), 500   
