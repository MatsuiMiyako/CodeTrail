from flask import Flask, Blueprint, render_template

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
    return render_template("lessons.html")

@main.route("/about/")
def about():
    return render_template("about.html")

# Register the Blueprint with the Flask app
app.register_blueprint(main)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
