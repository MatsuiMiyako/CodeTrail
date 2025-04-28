from flask import Flask, Blueprint, render_template, abort
import os
from .utils import categorize_lessons  # <— this is the cleaned-up helper

app = Flask(__name__)
main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/about/")
def about():
    return render_template("about.html")

@main.route("/lessons/")
def lessons():
    return render_template("lessons.html", lesson_data=categorize_lessons(app))

@main.route("/lessons/<lesson_name>")
def lesson(lesson_name):
    path = os.path.join(app.root_path, "templates", "lessons", f"{lesson_name}.html")
    if os.path.exists(path):
        return render_template(f"lessons/{lesson_name}.html")
    else:
        abort(404)

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
