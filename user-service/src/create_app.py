from flask import Flask
from src.api.routes import register_routes
from src.infrastructure.databases.db import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    init_db(app)
    register_routes(app)
    return app
