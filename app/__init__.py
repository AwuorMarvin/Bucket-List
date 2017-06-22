from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)
app.config['SECRET_KEY'] = 'asamplerandomstring'
# app.config['USERNAME'] = []
# app.config['PASSWORD'] = []
app.config['CREDENTIALS'] = {}
# Load the views
from app import views
from app import forms

def create_app(config_name):
    login_manager.init_app(app)
    login_manager.login_message = "Please login to access this page"
    login_manager.login_view = "auth.login"

    return app

# Load the config file
app.config.from_object('config')