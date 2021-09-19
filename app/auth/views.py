from flask import render_template, session, redirect, url_for, flash, request
from flask_login import login_user
from . import auth
from app.models import User
from app.auth.forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            user.update_session()
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('home.index')
            return redirect(next)
        flash("Wrong email or password.")
    return render_template('auth/login.html')