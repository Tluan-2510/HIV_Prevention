from src.infrastructure.models.user import User
from src.infrastructure.databases.db import db

def create_user(email, hashed_password):
    user = User(email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def find_by_email(email):
    return User.query.filter_by(email=email).first()
