"""Import module to render the html"""
from flask import render_template, redirect, url_for, flash, session, g
from app import app

from .forms import RegisterForm, LoginForm
from .models import User

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
    user = User()
    if form.validate_on_submit():
        session.pop('user', None)
        if user.create_user()['username'] == form.username.data and user.create_user()['password'] == form.password.data:
            flash('You were successfully logged in')
            session['user'] = form.username.data
            return render_template('profile.html', form=form)
        flash("Please check your details and try again")
    return render_template('login.html', form=form)

@app.route('/signup/', methods=["GET", "POST"], strict_slashes=False)
def signup():
    """Defines the route for the signup page"""
    form = RegisterForm()
    if form.validate_on_submit():
        return render_template('login.html')
    else:
        return render_template('signup.html', form=form)
    return render_template('signup.html', form=form)

@app.route('/profile')
def profile():
    """Defines the route for the profile page"""
    if g.user:
        return render_template('profile.html')
    else:
        return render_template('home.html')
@app.route('/add_bucketlist')
def add_bucketlist():
    """Defines the route for the add bucketlist page"""
    return render_template('add_bucketlist.html')

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    else:
        return render_template('home.html')

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
#Handle errors where a template is missing
@app.errorhandler(404)
def not_found_error(error):
    """Defines the route for the 404 page"""
    error = error
    return render_template('404.html'), 404
