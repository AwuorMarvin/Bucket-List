from flask import Flask, request
from flask_bootstrap import Bootstrap

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)
app.config['SECRET_KEY'] = 'asamplerandomstring'
app.config['USERNAME'] = []
app.config['PASSWORD'] = []
# Load the views
from app import views
from app import forms
