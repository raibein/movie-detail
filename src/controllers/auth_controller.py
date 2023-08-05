from src import app
from flask_jwt_extended import jwt_required

from src.services.auth_service import user_register, user_login, user_logout, get_all_users, get_logged_user, get_refresh_token, get_user_by_id, update_user_password



url_prefix = "/api/v1/auth"



'''Authentication for the User'''

def auth_page():

    '''New user login by Email, Username and Encrypted Password'''
    @app.route(url_prefix + '/register', methods=['POST'])
    def register():
       return user_register()




    '''Login by email and encrypted password'''
    @app.route(url_prefix + '/login', methods=['POST'])
    def login():
        return user_login()
    


    '''Logout from the system'''
    @app.route(url_prefix + '/logout', methods=['POST'])
    @jwt_required()
    def logout():
        return user_logout()




    '''Fetch all users'''
    @app.route(url_prefix + '/users', methods=['GET'])
    @jwt_required()
    def users():
        return get_all_users()



    '''Fetch logged user'''
    @app.route(url_prefix + '/user', methods=['GET'])
    @jwt_required()
    def logged_user():
        return get_logged_user()
    


    '''Fetch user by ID'''
    @app.route(url_prefix + '/user/<int:id>', methods=['GET'])
    @jwt_required()
    def user_by_id(id):
        return get_user_by_id(id)
    


    '''Change Password of the Logged User'''
    @app.route(url_prefix + '/user/password', methods=['PUT'])
    @jwt_required()
    def user_password_by_id():
        return update_user_password()
    


    '''Generate refresh token'''
    @app.route(url_prefix + '/token/refresh', methods=['GET'])
    @jwt_required(refresh=True)
    def refresh_token():
        return get_refresh_token()