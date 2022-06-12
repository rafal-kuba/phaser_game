from flask import render_template, session, redirect, url_for
from flask_login import login_required
from . import home

@home.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@home.route('/arts', methods=['GET'])
# @login_required
def arts():
    return render_template('arts.html')