from flask import Flask, jsonify, request, session
from passlib.hash import pbkdf2_sha256 
import uuid
from app import db
class User:
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signout(self):
        if(session.get('logged_in')):
            session.clear()
        return jsonify({"message": "Successfully signed out"}), 200    

    def signup(self):
        print(request.json)
        #create user
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.json.get('name'),
            "email": request.json.get('email'),
            "password": request.json.get('password') 
        }
        #encrypt user password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if(db.users.find_one({"email": user['email']})):
            return jsonify({"error": "Email address already in use"}), 400
        if(db.users.insert_one(user)):
            return self.start_session(user)
        return jsonify({"error": "Signup Failed"}), 400   

    def login(self):
        user = db.users.find_one({
            "email": request.json.get('email')
        })  

        if user and pbkdf2_sha256.verify(request.json.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({"error": "Invalid Login Credentials"}), 401       