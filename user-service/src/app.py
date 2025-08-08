from flask import Flask
from src.api.routes.user_routes import user_bp
from src.config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Đăng ký blueprint
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5001)
