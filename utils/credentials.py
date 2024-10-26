import os

from dotenv import load_dotenv

load_dotenv()


def get_database_credentials_dict() -> dict:
    dd = {
        "database_uri": os.getenv("DATABASE_URI"),
        "jwt_secret_key": os.getenv("JWT_SECRET_KEY")
    }
    return dd


def get_server_configuration_dict() -> dict:
    """
    Contains information about the server configuration, like port, current environment (local or prod)
    :return: config dict
    """
    dd = {
        "environment": os.getenv("ENVIRONMENT"),
        "port": os.getenv("PORT"),
    }
    return dd
