from src import app

def welcome_page():
    @app.route('/')
    def welcome():
        return {"message": "Welcome Page"}
