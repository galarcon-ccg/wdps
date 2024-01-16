from flask import Flask
from .sites.routes import wdps

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(wdps)
    
    return app