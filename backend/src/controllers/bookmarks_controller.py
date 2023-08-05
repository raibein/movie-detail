from src import app
from flask_jwt_extended import jwt_required

url_prefix = "/api/v1/bookmarks"

def bookmark_page():
    @app.route(url_prefix + '/')
    # @jwt_required()
    def bookmark():
        return {"message": "Bookmark Page"}