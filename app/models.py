from flask import request
from .forms import LoginForm

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.app_users = {'Username': self.username, 'Password': self.password}

    def login_user(self, username, password):
        if self.app_users[self.username] == self.password:
           return True
        else:
            return False