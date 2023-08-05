from src.controllers.swagger_controller import swagger_page
from src.controllers.welcome_controller import welcome_page
from src.controllers.auth_controller import auth_page
from src.controllers.bookmarks_controller import bookmark_page
from src.controllers.movie_controller import movie_page

def main():
    swagger_page()
    welcome_page()
    auth_page()
    bookmark_page()
    movie_page()
    