from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register routes after app is created
    from .routes import main
    app.register_blueprint(main)

    return app
