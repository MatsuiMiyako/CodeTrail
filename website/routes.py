from flask import Flask, Blueprint, render_template, abort
import os

# Create the Flask app instance
app = Flask(__name__)

# Create the Blueprint for main routes
main = Blueprint('main', __name__)

# Define your routes inside the Blueprint
@main.route("/")
def home():
    return render_template("home.html")

@main.route("/lessons/")
def lessons():
    # List all lesson files in the 'lessons' folder
    lessons_folder = os.path.join(app.root_path, 'templates', 'lessons')
    lessons_list = [f for f in os.listdir(lessons_folder) if f.endswith('.html')]
    return render_template("lessons.html", lessons=lessons_list)

@main.route("/lessons/<lesson_name>")
def lesson(lesson_name):
    # Check if the lesson file exists
    lesson_path = os.path.join(app.root_path, 'templates', 'lessons', f'{lesson_name}.html')
    if os.path.exists(lesson_path):
        return render_template(f"lessons/{lesson_name}.html")
    else:
        abort(404)  # If the lesson doesn't exist, show a 404 error page

@main.route("/about/")
def about():
    return render_template("about.html")

# Register the Blueprint with the Flask app
app.register_blueprint(main)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
