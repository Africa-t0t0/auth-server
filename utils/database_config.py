from utils import credentials

CREDENTIALS_DD = credentials.get_database_credentials_dict()

class Config:
    SQLALCHEMY_DATABASE_URI = CREDENTIALS_DD["database_uri"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = CREDENTIALS_DD["jwt_secret_key"]