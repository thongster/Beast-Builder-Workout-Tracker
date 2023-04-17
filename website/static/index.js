function deleteWorkout(workoutId) {
    fetch('/delete-workout', {
        method: 'POST',
        body: JSON.stringify({ workoutId: workoutId })
    }).then((_res) => {
        window.location.href = '/tracker';
    });
}