# Beast Builders Workout Tracker
#### Video Demo:  <https://youtu.be/bxitlJzCuVI>
#### Description: A walkthrough of the Beast Builders Workout Tracker created with Python and Flask.
This project is a simple CRUD (create, read, update, delete) app I created for the CS50x final project. Using a combination of Python, Flask, SQL, along with HTML, CSS (Bootstrap), and a tiny bit of Javascript, I was able to create a very simple workout tracker to replace my current workout tracking on an Excel spreadsheet.

The app uses a lot of what we learned throughout the CS50x course, particularly in week 8-9. Although this project is very simple, I am proud I was able to weave together much of the course material into an application that is actually useful in my life.

Starting with the HTML files, these were straight-forward for the most part. I used Bootstrap to style the CSS and it helped me to focus more on code and functionality rather than looks and design. The hardest parts of the HTML files were of course the Jinja parts, particularly in the layout.html and tracker.html file. For the layout, I had to figure out how to created the if/else statement to show the certain elements of the navbar when you were logged in vs. when you are not logged in. For the tracker, believe it or not the formatting was very difficult. But beyond that, I struggled with the simple for loop and Javascript to delete the button a lot. It could be the way I was naming my database, but it took a long time to work out that loop to display all the data.

In the auth.py file, I got a lot of the logic for login requirements from Problem Set 9. I still had to look around the web and learn to implement the werkzeug.security and also how to commit to a database as I was using SQLAlchemy (wanted to learn something different) and the code was not exactly the same as it was using SQLite3 in the cs50 codespace.

In the models.py file, I created the databases I needed to store Users, along with related user data I called Workout. That was done through the db.Relationship line. I spent a lot of time deleting the database and recreating the database so that the types of data would match what I was trying to input from the user's end.

The views.py file was the greatest challenge of the whole project. Looking at it now the code looks really simple, but I had weeks of bugs and a lot of discouragement trying to figure this out. Even with help from stackoverflow and scouring the web, thing just didn't seem to fit together. I finally got that the request.form.get would grab data from the forms in my html, then I had to figure out a way to display all the data together in 1 go. I initally had line 34-36 repeated 6 times for the date, exercise, sets, reps, weight, and workout, til I finally realized I could separate by commas. The final line in that route to order the workouts in descending order by id took me a while to figure out as well. The delete_workout function was also very challenging to complete. I had to look for examples online on how to use jsons and return jsonify. It took some copy and pasting and revising to my specific situation. 

The index.js file is a simple Javascript program that sends a POST request to the /delete-workout route. This then deletes the workout with the id called. It then redirects back to /tracker. As we did not focus on Javascript in the course, I had to go a learn some Javascript and frankenstein together some code I found online. This was also a weak part of my understanding and I am looking forward to learning more Javascript.

Overall, I am very happy I was able to get this done. Especially because it took a lot of brain power and the tying together of multiple subjects over the weeks of CS50. To be honest, if I had to code it all again it would certainly be a challenge but I think the more reps I get of coding different proejcts and problem solving bugs the more fluent I will get. It's been a pleasure.
