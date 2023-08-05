from src import app
from flask_jwt_extended import jwt_required

from src.services.movie_service import get_all_movies, create_movie, get_movie_by_id, update_movie_by_id, delete_movie_by_id

url_prefix = "/api/v1"


'''All Movies Details'''

def movie_page():
    
    '''Fetch all Movies'''
    @app.route(url_prefix + '/movies', methods=['GET'])
    def movies():
       return get_all_movies()



    '''Fetch movie by ID'''
    @app.route(url_prefix + '/movie/<int:id>', methods=['GET'])
    def movie_by_id(id):
        return get_movie_by_id(id)
    


    '''Add New Movie in the List'''
    @app.route(url_prefix + '/movie/add', methods=['POST'])
    @jwt_required()
    def movie():
        return create_movie()



    '''Update Movie by ID'''
    @app.route(url_prefix + '/movie/update/<int:id>', methods=['PUT'])
    @jwt_required()
    def movie_update_by_id(id):
        return update_movie_by_id(id)
    


    '''Delete Movie by ID'''
    @app.route(url_prefix + '/movie/delete/<int:id>', methods=['DELETE'])
    @jwt_required()
    def movie_delete_by_id(id):
        return delete_movie_by_id(id)
    

