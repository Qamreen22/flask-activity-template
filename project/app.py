# TODO Build the app.py file along with the template.html file to create a simple To-Do List app
# The app should have routes for adding a task, and should show a list of tasks
# Everything you have learned above will be useful for this task
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# List to store tasks
tasks = []
@app.route('/')
def home():
 return render_template('home.html', tasks=tasks)
@app.route('/add', methods=['POST'])
def add_task():
 task = request.form['task']
 tasks.append(task)
 return redirect(url_for('home'))
if __name__ == '__main__':
 app.run(debug=True)
