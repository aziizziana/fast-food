from flask import request, make_response, jsonify
from app.model.user import User
from app.application import Application
from . import app



@app.route("/")
def home():
    return "Welcome to fast foods"

@app.route("/signup", methods=['POST'])
def signup():
    if request.content_type != "application/json":
        return make_response(jsonify({
            "message":"Please use json as content type"
        })),400


    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    
    print('{}, {}, {}, {}'.format(first_name, last_name, email, password))
    return make_response(jsonify({
        "message":"successfully registered the user"
    })), 201