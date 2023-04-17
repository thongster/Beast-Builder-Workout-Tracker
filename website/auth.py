from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# Create a Blueprint object
auth = Blueprint('auth', __name__)

# define views for login, logout, and register
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get data from the html form
        username = request.form.get('username')
        password = request.form.get('password')

        # check user exists
        user = User.query.filter_by(username=username).first()
        # if user is found, check password is same as hashed password
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                # log the user in using flask_login
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Username does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # get data from the html form
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', category='error')
        # user and password validation
        elif len(username) < 4:
            flash('Username must be greater than 4 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        elif len(confirmation) < 7:
            flash('Password confirmation must be greater than 7 characters.', category='error')
        elif password != confirmation:
            flash('Passwords do not match.', category='error')
        else:
            # add new user to the database
            new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.tracker'))

    return render_template("register.html", user=current_user)