from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)
app.config['SECRET_KEY'] = 'asamplerandomstring'
# Load the views
from app import views

def create_app(config_name):
    login_manager.init_app(app)
    login_manager.login_message = "Please login to access this page"
    login_manager.login_view = "auth.login"

    return app

# Load the config file
app.config.from_object('config')