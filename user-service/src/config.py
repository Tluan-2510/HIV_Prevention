import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    SECRET_KEY = os.getenv('JWT_SECRET', 'default_secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
