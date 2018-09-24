from flask import request, make_response, jsonify
from . import app 
from app.model.user import User
from app.application import Application
from . import app

application = Application()

@app.route("/")
def home:
    return "Welcome to Fast Food Fast"

@app.route('/signup', methods=['POST'])
def signup():
    if request.content_type != 'application/json':
        return make_response(jsonify({
            "response": "Use json as content type"
        })) 400


    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    admin = data.get('admin')
    user = User(first_name, last_name, email, password, admin)
    application.register(user)
    print(application.users)
    return make_response(jsonify({
        'message':'successfully registered User'
    })), 201

@app.route('/login', methods=['POST'])
def login():
     if request.content_type != 'application/json':
        return make_response(jsonify({
            "response": "Use json as content type"
        })) 400

     data = request.get_json()
     email = data.get('email')
     password = data.get('password')

     if not application.does_user_exist(email):
         return make_response({
             "message":"User does not exist"
         }), 400

     if not application.login(email, password):
         return make_response({
             "message":"Invalid Credentials"
         }), 400

     user = application.get_user(email)
     token = user.get_token()
     return make_response(jsonify({
         "message": "successfully logged in"
         "token":token
        }))
    
    
