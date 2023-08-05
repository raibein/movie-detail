from flask import request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, HTTP_201_CREATED, HTTP_200_OK
import validators

from src.database import db
from src.database.user import User

from flask_jwt_extended import get_jwt_identity, create_access_token, create_refresh_token, unset_jwt_cookies






'''New user login by Email, Username and Encrypted Password'''
def user_register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if len(password) < 6:
        return jsonify({
            "error": "Password must be at leat 8 characters"
        }), HTTP_400_BAD_REQUEST

    if len(username) < 3:
        return jsonify({
            "error": "Username is too short"
        }), HTTP_400_BAD_REQUEST

    if not username.isalnum() or " " in username:
        return jsonify({
            "error": "Username should be alphanumeric, also no spaces"
        }), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({
            "error": "Email is not valid"
        }), HTTP_400_BAD_REQUEST

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({
            "error": "Email is already registered, please use another email"
        }), HTTP_409_CONFLICT
    
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({
            "error": "Username is already registered, please use another email"
        }), HTTP_409_CONFLICT

    pwd_hash = generate_password_hash(password)
    user = User(username=username, password=pwd_hash, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User created",
        "data": {
            "username": username,
            "email": email
        }
    }), HTTP_201_CREATED






'''Login by email and encrypted password'''
def user_login():
    email = request.json.get('email', '')
    password = request.json.get('password', '')

    user = User.query.filter_by(email=email).first()

    if user:
        is_pass_correct = check_password_hash(user.password, password)

        if is_pass_correct:
            access_token = create_access_token(identity = user.id)
            refresh_token = create_refresh_token(identity = user.id)
            
            return jsonify({
                "status": "success",
                "data": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "username": user.username,
                    "email": user.email
                }
            })

    return jsonify({
        "status": "error",
        "message": "Worng Credential"
    }), HTTP_401_UNAUTHORIZED





'''Login by email and encrypted password'''
def user_logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return jsonify({
        "status": "success",
        "message": "Successfully Logout"
    }), HTTP_200_OK





'''Fetch all users'''
def get_all_users():
    users = User.query.all()

    data = []

    if users:
        for user in users:
            data.append({      
                    "user": user.username,
                    "email": user.email
                })
        return jsonify({
            "status": "success",
            "data": data
        }), HTTP_200_OK

    return jsonify({
            "status": "error",
            "message": "Could not fetch the data"
        }), HTTP_400_BAD_REQUEST



'''Fetch logged user'''
def get_logged_user():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if user:
        return jsonify({
                "status": "success",
                "data": {
                    "user": user.username,
                    "email": user.email
                }
            }), HTTP_200_OK
            

    return jsonify({
            "status": "error",
            "message": "Could not fetch the user data"
        }), HTTP_400_BAD_REQUEST




'''Fetch user by ID'''
def get_user_by_id(id):
    user = User.query.filter_by(id=id).first()

    if user:
        return jsonify({
                "status": "success",
                "data": {
                    "user": user.username,
                    "email": user.email
                }
            }), HTTP_200_OK
            

    return jsonify({
            "status": "error",
            "message": "Could not fetch the user data"
        }), HTTP_400_BAD_REQUEST



'''Update logged user password'''
def update_user_password():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if user:
        username  = user.username
        email     = user.email
        password  = request.json['password']

        if len(password) < 6:
            return jsonify({
                "error": "Password must be at leat 8 characters"
            }), HTTP_400_BAD_REQUEST
        
        user.username  = username
        user.email     = email
        pwd_hash       = generate_password_hash(password)

        user.password = pwd_hash
        
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Update password successfully",
            "data": {
                "username": username,
                "email": email
            }
        }), HTTP_200_OK

    return jsonify({
            "status": "error",
            "message": "Could not update password for the '{username}' "
        }), HTTP_400_BAD_REQUEST






'''Generate refresh token'''
def get_refresh_token():
    user_id = get_jwt_identity()
    access_token = create_access_token(identity = user_id)

    if user_id:
        return jsonify({
                "status": "success",
                "data": {
                    "access_token": access_token
                }
            }), HTTP_200_OK
            

    return jsonify({
            "status": "error",
            "message": "Could not generate refresh token"
        }), HTTP_400_BAD_REQUEST