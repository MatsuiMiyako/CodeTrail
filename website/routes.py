from flask import Flask, Blueprint, render_template, abort
from jinja2 import TemplateNotFound  # Add this import
import os
from .utils import categorize_lessons

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

@main.route("/lessons/<category>/<lesson_name>")
def lesson(category, lesson_name):
    folder_map = {
        "python": "python",
        "music-theory": "music",
        "pixel-art": "pixel_art",
        "precalculus": "precal",
        "bash": "bash",
        "networking": "networking"
    }
    
    if category not in folder_map:
        abort(404)
        
    try:
        return render_template(f"lessons/{folder_map[category]}/{lesson_name}.html")
    except TemplateNotFound:
        abort(404)

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)