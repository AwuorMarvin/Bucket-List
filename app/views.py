from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

#Handle errors where a template is missing
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
