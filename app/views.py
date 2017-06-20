"""Import module to render the html"""
from flask import render_template
from app import app

from .auth.forms import RegisterForm, LoginForm

@app.route('/')
def index():
    """Defines the route for the home page"""
    return render_template('home.html')

@app.route('/about')
def about():
    """Defines the route for the about page"""
    return render_template('about.html')

@app.route('/login/', methods=["GET", "POST"], strict_slashes=False)
def login():
    
    """Defines the route for the login page"""
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('profile.html')
    return render_template('login.html')

@app.route('/signup/', methods=["GET", "POST"], strict_slashes=False)
def signup():
    """Defines the route for the signup page"""
    form = RegisterForm()
    if form.validate_on_submit():
        return '<h1> Hello' + form.username.data + '.</h1>' 
    return render_template('signup.html', form=form)

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
