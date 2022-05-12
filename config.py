import os
class Config:    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://april:2222@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://april:2222@localhost/pitch'

class TestConfig(Config):
    
    pass

class DevConfig(Config):
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
