from flask import request, jsonify
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, HTTP_201_CREATED, HTTP_200_OK

from src.database import db
from src.database.movie import Movie

from flask_jwt_extended import get_jwt_identity




'''Add new Movie into the database'''
def create_movie():
    name = request.json['name']
    short_desc = request.json['short_desc']
    description = request.json['description']
    release_date = request.json['release_date']
    rating = request.json['rating']
    user_id = get_jwt_identity()

    if Movie.query.filter_by(name=name).first() is not None:
        return jsonify({
            "error": "Movie is already in the database, please add another movie name"
        }), HTTP_409_CONFLICT

    movie = Movie(  name=name, 
                    short_desc=short_desc,
                    description=description,
                    release_date=release_date,
                    rating=rating,
                    user_id=user_id
                )
    db.session.add(movie)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Movie has successfully added to the database",
        "data": {
            "name": name,
            "short_desc": short_desc,
            "description": description,
            "release_date": release_date,
            "rating": rating
        }
    }), HTTP_201_CREATED



'''Fetch all Movies in the list'''
def get_all_movies():
    movies = Movie.query.all()

    data = []

    if movies:
        for movie in movies:
            data.append({
                    "id": movie.id,
                    "name": movie.name,
                    "user_id": movie.user_id,
                    "slug": movie.slug,
                    "short_desc": movie.short_desc,
                    "description": movie.description,
                    "release_date": movie.release_date,
                    "rating": movie.rating,
                })
        return jsonify({
            "status": "success",
            "data": data
        }), HTTP_200_OK

    return jsonify({
            "status": "error",
            "message": "Could not fetch the data"
        }), HTTP_400_BAD_REQUEST




'''Fetch Movie by ID'''
def get_movie_by_id(id):
    movie = Movie.query.filter_by(id=id).first()

    if movie:
        return jsonify({
                "status": "success",
                "data": {
                    "id": movie.id,
                    "name": movie.name,
                    "user_id": movie.user_id,
                    "slug": movie.slug,
                    "short_desc": movie.short_desc,
                    "description": movie.description,
                    "release_date": movie.release_date,
                    "rating": movie.rating,
                }
            }), HTTP_200_OK
            

    return jsonify({
            "status": "error",
            "message": "Could not fetch any data"
        }), HTTP_400_BAD_REQUEST



'''Update Movie by ID'''
def update_movie_by_id(id):
    data = Movie.query.filter_by(id=id).first()

    if data:
        user_id         = get_jwt_identity()
        name            = request.json['name']
        short_desc      = request.json['short_desc']
        description     = request.json['description']
        release_date    = request.json['release_date']
        rating          = request.json['rating']
        
        data.name           = name
        data.short_desc     = short_desc
        data.description    = description
        data.release_date   = release_date
        data.rating         = rating
        data.user_id        = user_id

        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Update movie successfully",
            "data": {
                "user_id": user_id,
                "name": name,
                "short_desc": short_desc,
                "description": description,
                "release_date": release_date,
                "rating": rating
            }
        }), HTTP_200_OK

    return jsonify({
            "status": "error",
            "message": "Could not update movie"
        }), HTTP_400_BAD_REQUEST



'''Delete Movie by ID'''
def delete_movie_by_id(id):
    data = Movie.query.filter_by(id=id).first()

    if data:
        db.session.delete(data)
        db.session.commit()

        return jsonify({
               "status": "success",
                "message": "Delete movie successfully"
            }), HTTP_200_OK

    return jsonify({
            "status": "error",
            "message": "Could not delete data"
        }), HTTP_400_BAD_REQUEST