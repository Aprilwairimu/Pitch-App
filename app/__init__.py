from config import config_options
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from .models import User

db = SQLAlchemy()
# mail = Mail()# 
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'
def create_app():
    app = Flask(__name__)
    db.init_app(app) 
      
    # Creating the app configurations
    # app.config.from_object(config_options[config_name])    
    # #Initializing Flask Extensions
    
    # login_manager.init_app(app)
    # mail.init_app(app)    
    #  login_manager=LoginManager()
    # login_manager.login.view ="auth.login"
    # login_manager.init_app(app)    
# @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))    
    from .views import views
    from .auth import auth    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')    
    return app