from Flask import render_template, request, redirect, url_for

from . import app, db

from .models import User, Goal

@app.route('/')
def index():
    return 'Welcome to the Goal Tracker!!'