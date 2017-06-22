"""Import module to render the html"""
from flask import render_template, redirect, url_for, flash, session, g, request
from app import app

from .forms import RegisterForm, LoginForm
from .models import User

dictionary = {}
# new_user = User()

@app.route('/')
def index():
    """Defines the route for the home page"""
    return render_template('home.html')

@app.route('/about')
def about():
    """Defines the route for the about page"""
    return render_template('about.html')

@app.route('/login', methods=["GET", "POST"], strict_slashes=False)
def login():
    """Defines the route for the login page"""
    form = LoginForm()
    if form.validate_on_submit():
        session.pop('user', None)
        if form.username.data in app.config['USERNAME'] and form.password.data in app.config['PASSWORD']:
            flash('You were successfully logged in')
            session['user'] = form.username.data
            return render_template('profile.html')
        else:
            flash("Please check your details and try again")
            render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/signup/', methods=["GET", "POST"], strict_slashes=False)
def signup():
    """Defines the route for the signup page"""
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data

        app.config['USERNAME'].append(username)
        app.config['PASSWORD'].append(password)

        flash('Signed up as {}, please log in to continue'.format(username))
        return redirect(url_for('login'))
    else:
        return render_template('signup.html', form=form)

@app.route('/profile')
def profile():
    """Defines the route for the profile page"""
    # profile= {}
    if g.user:
        return render_template('profile.html', data=dictionary)
    else:
        return render_template('home.html')
@app.route('/add_bucketlist', methods=['GET', 'POST'])
def add_bucketlist():
    """Defines the route for the add bucketlist page"""
    bucketlist = {}
    if request.method == "POST":
        title = request.form['inputTitle']
        description = request.form['inputDescription']

        bucketlist['title'] = title
        bucketlist['body'] = description
        
        return render_template('profile.html', data=bucketlist)
    else:
        return render_template('add_bucketlist.html', data=bucketlist)

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

# @app.route('/getsession')
# def getsession():
#     if 'user' in session:
#         return session['user']
#     else:
#         return render_template('home.html')

# @app.route('/dropsession')
# def dropsession():
#     session.pop('user', None)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
#Handle errors where a template is missing
@app.errorhandler(404)
def not_found_error(error):
    """Defines the route for the 404 page"""
    error = error
    return render_template('404.html'), 404
