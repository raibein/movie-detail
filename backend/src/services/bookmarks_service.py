from src import app

url_prefix = "/api/v1/bookmarks"

def bookmark_page():
    @app.route(url_prefix + '/')
    def bookmark():
        return {"message": "Bookmark Page"}