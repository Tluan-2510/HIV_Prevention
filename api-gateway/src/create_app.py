from flask import Flask
from src.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix='/user')
    return app
