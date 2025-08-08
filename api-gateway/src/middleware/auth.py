import jwt
from flask import request, jsonify
from src.config import Config

def require_auth(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        try:
            jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
        except Exception:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper
