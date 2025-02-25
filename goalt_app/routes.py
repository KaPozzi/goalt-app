from flask import render_template, request, redirect, url_for, Blueprint, flash, session
from .database import create_user, create_goal, get_user
from .database import get_users

# from . import app, db

from .models import User, Goal

## This file is destinated to set each page and it's backend logic ##

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('home.html')


@routes.route('/register', methods=['GET', 'POST'])
def register_user():
    users = get_users()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        create_user(username, password)
        flash(f'User created successfully. {username}')
        return redirect(url_for('routes.register_user'))
    else:
        print(users)
        return render_template('register.html', users=users)
    
@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username, password)
        if user:
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Invalid credentials')
            return redirect(url_for('routes.login'))
    return render_template('login.html')

@routes.route('/goals')
def goals_page():
    return render_template('goals.html')