import jwt, bcrypt
from datetime import datetime, timedelta
from src.repositories.user_repository import create_user, find_by_email
from src.config import Config

def register_user(email, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return create_user(email, hashed.decode())

def login_user(email, password):
    user = find_by_email(email)
    if not user or not bcrypt.checkpw(password.encode(), user.password.encode()):
        raise Exception("Invalid credentials")
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return token
