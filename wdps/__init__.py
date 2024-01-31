import os
import ssl
from flask import Flask
from .sites.routes import wdps, gene
from .apis.routes import api
from flask_cors import CORS


ssl._create_default_https_context = ssl._create_unverified_context
#Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
gql_url = os.environ.get("GQL_SERVICE")

def create_app():
    app = Flask(__name__)
    CORS(app)
    #GraphQL client configuration
    #gql_url = os.environ.get("GQL_SERVICE")
    #browser_url = os.environ.get("REGULONDB_BROWSER")
    #gql_service = HTTPEndpoint(gql_url)
    #Blueprints configuration
    app.register_blueprint(wdps)
    app.register_blueprint(api)
    app.register_blueprint(gene)

    return app