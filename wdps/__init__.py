from flask import Flask
from .sites.routes import wdps
from .apis.routes import api
from flask_cors import CORS
from sgqlc.endpoint.http import HTTPEndpoint

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(wdps)
    app.register_blueprint(api)
        
    return app