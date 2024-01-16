from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/wdps/api')

@api.route("/")
def index():
    return "welcome RegulonDB-WDPS-APIS"

@api.route("/dtt")
def index_dtt():
    return "welcome DTT serve"