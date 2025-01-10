from flask import render_template, request, redirect, url_for

from . import app, db

from .models import User, Goal

@app.route('/')
def home():
    return render_template('home.html')