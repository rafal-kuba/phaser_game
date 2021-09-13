from flask import render_template, session, redirect, url_for
from . import home

@home.route('/', methods=['GET'])
def index():
    return render_template('home.html')