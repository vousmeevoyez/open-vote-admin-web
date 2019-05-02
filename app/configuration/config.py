"""
    Configuration
    _______________
    This is module for storing all configuration for various environments
"""
import os

basedir = os.path.abspath(os.path.dirname("data"))

class Config:
    SECRET_KEY = 'jaslkdjklajskldjlasjdljasljl'
    DATABASE = {
        "DRIVER"   : os.getenv('DB_DRIVER') or "postgresql://", # sqlite // postgresql // mysql
        "USERNAME" : os.getenv('DB_USERNAME') or "prci",
        "PASSWORD" : os.getenv('DB_PASSWORD') or "passsword",
        "HOST_NAME": os.getenv('DB_HOSTNAME') or "localhost",
        "DB_NAME"  : os.getenv('DB_NAME') or "db_prci",
    }

    UPLOAD_FOLDER = basedir + "/data"

    ALLOWED_EXTENSIONS = set(['pdf'])

    SENTRY_CONFIG = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GRPC_CHANNEL = os.getenv("GRPC_CHANNEL") or "127.0.0.1:5001"

    JWT_SECRET = os.getenv("JWT_SECRET") or "some_jwt_secret"

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None
#end class


class DevelopmentConfig(Config):
    """ This is class for development configuration """
    DEBUG = True

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
            DATABASE["DB_NAME"] + "_dev"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
#end class


class TestingConfig(Config):
    """ This is class for testing configuration """
    DEBUG = True
    TESTING = True

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
            DATABASE["DB_NAME"] + "_testing"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SENTRY_CONFIG = {}
#end class


class ProductionConfig(Config):
    """ This is class for production configuration """
    DEBUG = False

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
            DATABASE["DB_NAME"] + "_prod"
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    SENTRY_CONFIG = Config.SENTRY_CONFIG
    SENTRY_CONFIG["dsn"] = os.environ.get("SENTRY_DSN")
#end class

CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
