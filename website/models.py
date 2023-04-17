from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# define database schema for workout notes
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=True)
    exercise = db.Column(db.String(200), nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.String(50), nullable=True)
    weight = db.Column(db.String(50), nullable=True)
    note = db.Column(db.String(5000), nullable=True)
    # create a relationship between the user and the workout tables through the foregin key id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# define database schema
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    # create a relationship to track which workouts are for which user
    workouts = db.Relationship('Workout')

