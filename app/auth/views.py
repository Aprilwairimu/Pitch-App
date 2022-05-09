from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')