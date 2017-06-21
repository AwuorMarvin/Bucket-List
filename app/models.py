from flask import request
from .forms import LoginForm
class User(object):
    def __init__(self):
        self.username = 'request.form.get(LoginForm.username)'
        self.password = 'request.form.get(LoginForm.password)'

    def create_user(self):
        self.user = User()
        self.user_details = self.user.__dict__
        return self.user_details
    