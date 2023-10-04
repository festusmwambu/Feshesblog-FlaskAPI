import os
from dotenv import load_dotenv



# Load the environment variables from `.env` module.
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


def as_bool(value):
    if value:
        return value.lower() in ['true', 'yes', 'on', '1']
    return False


# Common settings for all environments
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'top-secret!')
    USE_CORS = as_bool(os.environ.get('USE_CORS') or 'yes')
    CORS_SUPPORTS_CREDENTIALS = True

    # security options
    DISABLE_AUTH = as_bool(os.environ.get('DISABLE_AUTH'))
    ACCESS_TOKEN_MINUTES = int(os.environ.get('ACCESS_TOKEN_MINUTES') or '15')
    REFRESH_TOKEN_DAYS = int(os.environ.get('REFRESH_TOKEN_DAYS') or '7')
    REFRESH_TOKEN_IN_COOKIE = as_bool(os.environ.get(
        'REFRESH_TOKEN_IN_COOKIE') or 'yes')
    REFRESH_TOKEN_IN_BODY = as_bool(os.environ.get('REFRESH_TOKEN_IN_BODY'))
    RESET_TOKEN_MINUTES = int(os.environ.get('RESET_TOKEN_MINUTES') or '15')
    PASSWORD_RESET_URL = os.environ.get('PASSWORD_RESET_URL') or \
        'http://localhost:3000/reset'
    
    # API documentation
    APIFAIRY_TITLE = 'Feshesblog-FlaskAPI'
    APIFAIRY_VERSION = '1.0'
    APIFAIRY_UI = os.environ.get('DOCS_UI', 'elements')

    # email options
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.sendgrid.net')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or '587')
    MAIL_USE_TLS = as_bool(os.environ.get('MAIL_USE_TLS'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER',
                                       'donotreply@feshesblog.sendgrid.com')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')


# Development enviroment settings
class DevelopmentConfig(Config):
    DEBUG = True
    # database options
    ALCHEMICAL_DATABASE_URL = os.environ.get('DEVELOPMENT_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dev-db.sqlite')
    ALCHEMICAL_ENGINE_OPTIONS = {'echo': as_bool(os.environ.get('SQL_ECHO'))}

# Production environment settings
class ProductionConfig(Config):
    DEBUG = False
    # database options
    ALCHEMICAL_DATABASE_URL = os.environ.get('PRODUCTION_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'prod-db.sqlite')
    ALCHEMICAL_ENGINE_OPTIONS = {}

# Testing environment settings
class TestingConfig(Config):
    TESTING = True
    # database options
    ALCHEMICAL_DATABASE_URL = os.environ.get('TESTING_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test-db.sqlite')
    ALCHEMICAL_ENGINE_OPTIONS = {}

