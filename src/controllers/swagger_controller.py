from src import app
from flask import render_template

url_prefix = "/api/docs"


def swagger_page():

    @app.route(url_prefix + '/')
    def get_swagger_docs():
        # print('sending docs')
        return render_template('swaggerui.html')
