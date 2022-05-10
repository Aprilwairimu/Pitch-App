from config import config_options
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
# from .models import User

db = SQLAlchemy()
mail = Mail()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)

    #Initializing Flask Extensions
    db.init_app(app) 
    login_manager.init_app(app) 
    mail.init_app(app) 

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

   # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')



    return app