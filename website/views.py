from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Workout
from . import db
import json

# Create a Blueprint object
views = Blueprint('views', __name__)

# define views
@views.route('/')
def home():
    return render_template("home.html")
    
@views.route('/tracker', methods=['GET', 'POST'])
@login_required
def tracker():
    if request.method == 'POST':
        date = request.form.get('date')
        exercise = request.form.get('exercise')
        sets = request.form.get('sets')
        reps = request.form.get('reps')
        weight = request.form.get('weight')
        workout = request.form.get('workout')

        # if date is not empty
        if len(date) < 1:
            flash('Date is required.', category='error')
        # if exercise is not empty
        if len(exercise) < 1:
            flash('Exercise is required.', category='error')
        else:
            # add all info to database
            new_workout = Workout(date=date, exercise=exercise, sets=sets, reps=reps, weight=weight, note=workout, user_id=current_user.id)
            db.session.add(new_workout)
            db.session.commit()
            flash('Workout added. Keep going!', category='success')

    # Query the workouts for the current user and order them by id in descending order
    workouts = Workout.query.filter_by(user_id=current_user.id).order_by(Workout.id.desc()).all()

    return render_template("tracker.html", user=current_user, workouts=workouts)

@views.route('/delete-workout', methods=['POST'])
def delete_workout():
    # take in data from post request as json
    workout = json.loads(request.data)
    workoutId = workout['workoutId']
    workout = Workout.query.get(workoutId)
    if workout:
        if workout.user_id == current_user.id:
            db.session.delete(workout)
            db.session.commit()

    return jsonify({})