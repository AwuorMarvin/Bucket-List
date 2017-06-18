"""Import module to render the html"""
from flask import render_template
from app import app

@app.route('/')
def index():
    """Defines the route for the home page"""
    return render_template('home.html')

@app.route('/about')
def about():
    """Defines the route for the about page"""
    return render_template('about.html')

@app.route('/login')
def login():
    """Defines the route for the login page"""
    return render_template('login.html')

@app.route('/signup')
def signup():
    """Defines the route for the signup page"""
    return render_template('signup.html')

@app.route('/profile')
def profile():
    """Defines the route for the profile page"""
    return render_template('profile.html')

#Handle errors where a template is missing
@app.errorhandler(404)
def not_found_error(error):
    """Defines the route for the 404 page"""
    error = error
    return render_template('404.html'), 404
