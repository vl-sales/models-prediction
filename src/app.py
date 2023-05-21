from .routes import models_api
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.register_blueprint(models_api)
    return app
